import pandas as pd

timetable_to_time = {'January': "January",
                     'June': "June",
                     'July': "July",
                     'August': "August",
                     'E1A': "Mon 8-12",
                     'E2A': "Mon 13-17",
                     'E3A': "Tue 8-12",
                     'E4A': "Tue 13-17",
                     'E7': "Tue 18-22",
                     'E5A': "Wed 8-12",
                     'E5B': "Wed 13-17",
                     'E5': "Wed 8-17",
                     'E2B': "Thu 8-12",
                     'E1B': "Thu 13-17",
                     'E4B': "Fri 8-12",
                     'E3B': "Fri 13-17",
                     'F1A': "Mon 8-12",
                     'F2A': "Mon 13-17",
                     'F3A': "Tue 8-12",
                     'F4A': "Tue 13-17",
                     'F7': "Tue 18-22",
                     'F5A': "Wed 8-12",
                     'F5B': "Wed 13-17",
                     'F2B': "Thu 8-12",
                     'F1B': "Thu 13-17",
                     'F4B': "Fri 8-12",
                     'F3B': "Fri 13-17"}


def ects_above_required(courses, core, courselist):
    """Regner mængden af ects-point jeg har over det nødvendige i disse to lister:
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Core
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Courselist"""

    core_commons = pd.merge(current_courses, core["title"], how='inner')
    courselist_commons = pd.merge(current_courses, courselist["title"], how='inner')

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


def alternative_courses(current, core, courselist):
    """Find all courses that have not been taken from the core and courselist from the data science requirements"""

    # Remove all courses that are already being taken to show alternatives
    core_commons = pd.merge(current_courses, core["title"].reset_index(), how='inner').set_index('index')
    courselist_commons = pd.merge(current_courses, courselist["title"].reset_index(), how='inner').set_index('index')
    core_alts = core.drop(core_commons.index.values.tolist())
    courselist_alts = courselist.drop(courselist_commons.index.values.tolist())

    # Make timetable readable for easy user access
    core_alts['timetable_group'].replace(timetable_to_time, inplace=True)
    courselist_alts['timetable_group'].replace(timetable_to_time, inplace=True)

    print("Alternative course from core:", core_alts, sep='\n', end='\n\n')
    print("Alternative course from courselist:", courselist_alts, sep='\n', end='\n\n')


if __name__ == '__main__':

    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})
    core = pd.read_csv("data_science_requirements/core.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    courselist = pd.read_csv("data_science_requirements/courselist.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    # print(current_courses)
    ects_above_required(current_courses, core, courselist)
    # alternative_courses(current_courses, core, courselist)
