import pandas as pd

timetable_to_time = {'January': "January",
                     'June': "June",
                     'July': "July",
                     'August': "August",
                     'E1A': "Fall Mon 8-12",
                     'E2A': "Fall Mon 13-17",
                     'E3A': "Fall Tue 8-12",
                     'E4A': "Fall Tue 13-17",
                     'E7': "Fall Tue 18-22",
                     'E5A': "Fall Wed 8-12",
                     'E5B': "Fall Wed 13-17",
                     'E5': "Fall Wed 8-17",
                     'E2B': "Fall Thu 8-12",
                     'E1B': "Fall Thu 13-17",
                     'E4B': "Fall Fri 8-12",
                     'E3B': "Fall Fri 13-17",
                     'F1A': "Spring Mon 8-12",
                     'F2A': "Spring Mon 13-17",
                     'F3A': "Spring Tue 8-12",
                     'F4A': "Spring Tue 13-17",
                     'F7': "Spring Tue 18-22",
                     'F5A': "Spring Wed 8-12",
                     'F5B': "Spring Wed 13-17",
                     'F2B': "Spring Thu 8-12",
                     'F1B': "Spring Thu 13-17",
                     'F4B': "Spring Fri 8-12",
                     'F3B': "Spring Fri 13-17"}


def ects_above_required(courses, core, courselist):
    """Regner mængden af ects-point jeg har over det nødvendige i disse to lister:
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Core
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Courselist"""

    core_commons = pd.merge(courses, core["title"], how='inner')
    courselist_commons = pd.merge(courses, courselist["title"], how='inner')

    print("Total courses taken from core: ")
    print(core_commons, "\n")
    print("Total courses taken from courselist: ")
    print(courselist_commons, "\n\n")
    sum1 = sum(core_commons["points"])
    sum2 = sum(courselist_commons["points"])
    total1 = 15
    total2 = 45

    print(f"Points from core: {sum1}")
    print(f"Points from courselist: {sum2}\n\n")

    print(f"Core points over requirement: {sum1 - total1}")
    print(f"Courselist points over requirement: {sum2 - total2}\n")


def alternative_courses(current, core, courselist, num_points=None, time_period=None):
    """Find all courses that have not been taken from the core and courselist from the data science requirements"""

    # Remove all courses that are already being taken to show alternatives
    core_commons = pd.merge(current, core["title"].reset_index(), how='inner').set_index('index')
    courselist_commons = pd.merge(current, courselist["title"].reset_index(), how='inner').set_index('index')
    core_alts = core.drop(core_commons.index.values.tolist())
    courselist_alts = courselist.drop(courselist_commons.index.values.tolist())

    # Make timetable readable for easy user access
    core_alts['timetable_group'].replace(timetable_to_time, inplace=True)
    courselist_alts['timetable_group'].replace(timetable_to_time, inplace=True)
    # Find courses from courselist with specific number of ects points or in a specific period
    # courselist_alts = courselist_alts[courselist_alts["points"] == 5.0]
    is_fall = ["Fall" in time for time in courselist_alts["timetable_group"]]
    courselist_alts = courselist_alts[is_fall]
    five_points = [time == 7.5 for time in courselist_alts["points"]]
    courselist_alts = courselist_alts[five_points]

    print("Alternative course from core:", core_alts, sep='\n', end='\n\n')
    print("Alternative course from courselist:", courselist_alts, sep='\n', end='\n\n')


if __name__ == '__main__':

    current_courses = pd.read_csv("current_courses_oct22.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})
    core = pd.read_csv("data_science_requirements/core.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    courselist = pd.read_csv("data_science_requirements/courselist.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    # print(current_courses)
    ects_above_required(current_courses, core, courselist)
    alternative_courses(current_courses, core, courselist)