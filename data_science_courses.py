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
                     'E6B': "Wed 13-17",
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
                     'F6B': "Wed 13-17",
                     'F2B': "Thu 8-12",
                     'F1B': "Thu 13-17",
                     'F4B': "Fri 8-12",
                     'F3B': "Fri 13-17",
}


def ects_above_required(courses, core, courselist):
    """Regner mængden af ects-point jeg har over det nødvendige i disse to lister:
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Core
    https://www.compute.dtu.dk/english/education/Data-Science-Big-Data/Courselist"""

    core_commons = pd.merge(current_courses, core["title"], how ='inner')
    courselist_commons = pd.merge(current_courses, courselist["title"], how ='inner')

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
    print(f"Courselist points over requirement: {sum2 - total2}")


def alternative_courses(current, core, courselist):
    """Find all courses that have not been taken from the core and courselist from the data science requirements"""

    core_commons = pd.merge(current_courses, core["title"], how ='inner')
    courselist_commons = pd.merge(current_courses, courselist["title"], how ='inner')
    core_alts = core[~core.isin(current)].dropna()
    courselist_alts = courselist[~courselist.isin(current)].dropna()

    print("Alternative course from core:")
    print(core_alts, "\n")
    print("Alternative course from courselist:")
    print(courselist_alts, "\n")

if __name__ == '__main__':
    
    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0:str, 1:str, 2:str, 3:float})
    core = pd.read_csv("core.csv", sep='\t', dtype={0:str, 1:str, 2:float, 3:str})
    courselist = pd.read_csv("courselist.csv", sep='\t', lineterminator='\r', dtype={0:str, 1:str, 2:float, 3:str})
    print(courselist["timetable_group"].unique())
    # print(current_courses)
    ects_above_required(current_courses, core, courselist)
    # alternative_courses(current_courses, core, courselist)
