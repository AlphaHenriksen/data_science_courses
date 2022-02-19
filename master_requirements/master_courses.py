import pandas as pd
import matplotlib.pyplot as plt

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
                     'F3B': "Fri 13-17",
}


def ects_requirements(current_courses, general_1, general_2, techno):
    """Undersøger om der er taget for få eller for mange kurser i teknologiske linjefag eller generelle kompetencer"""

    general_1_commons = pd.merge(current_courses, general_1["title"], how ='inner')
    general_2_commons = pd.merge(current_courses, general_2["title"], how ='inner')
    techno_commons = pd.merge(current_courses, techno["title"], how ='inner')
    names = ["entrepreneurship", "general competance", "technological specialization", "thesis"]

    print(f"Total courses taken from {names[0]}: ")
    print(general_1_commons, "\n")
    print(f"Total courses taken from {names[1]}: ")
    print(general_2_commons, "\n\n")
    print(f"Total courses taken from {names[2]}: ")
    print(techno_commons, "\n\n")
    print(f"Total courses taken from {names[3]}: ")
    print(current_courses[current_courses.title == "Master's Thesis"], "\n\n")
    totals = [sum(general_1_commons["points"]), sum(general_2_commons["points"]), sum(techno_commons["points"]), current_courses.points[current_courses.title == "Master's Thesis"].values[0]]
    neededs = [10, 20, 30, 30]

    for (name, total) in zip(names, totals):
        print(f"Points from {name}: {total}")
    print()

    for (total, needed, name) in zip(totals, neededs, names):
        if total >= needed:
            print(f"The requirements for {name} have been satisfied")
    print()
    
    print(f"The total number of ECTS points in the plan is {sum(current_courses.points) - 10}\n")  # Subtract 10 from total since these points are from the bachelor

    plt.bar(list(range(len(totals)-1)), [totals[0] + totals[1], totals[2], totals[3]], color = ["red", "purple", "orange"])
    plt.axhline(30, color = "k", linestyle = "--")
    plt.show()


def alternative_courses(current, core, courselist):
    """Find all courses that have not been taken from the core and courselist from the data science requirements"""

    # Remove all courses that are already being taken to show alternatives
    core_commons = pd.merge(current_courses, core["title"].reset_index(), how ='inner').set_index('index')
    courselist_commons = pd.merge(current_courses, courselist["title"].reset_index(), how ='inner').set_index('index')
    core_alts = core.drop(core_commons.index.values.tolist())
    courselist_alts = courselist.drop(courselist_commons.index.values.tolist())

    # Make timetable readable for easy user access
    core_alts['timetable_group'].replace(timetable_to_time, inplace=True)
    courselist_alts['timetable_group'].replace(timetable_to_time, inplace=True)

    print("Alternative course from core:")
    print(core_alts, "\n")
    print("Alternative course from courselist:")
    print(courselist_alts, "\n")

if __name__ == '__main__':
    
    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0:str, 1:str, 2:str, 3:float})
    general_1 = pd.read_csv("master_requirements\general_competence_1.csv", sep='\t', dtype={0:str, 1:str, 2:float, 3:str})
    general_2 = pd.read_csv("master_requirements\general_competence_2.csv", sep='\t', dtype={0:str, 1:str, 2:float, 3:str})
    techno = pd.read_csv("master_requirements/technological_specialization.csv", sep='\t', dtype={0:str, 1:str, 2:float, 3:str})

    # print(general_1)
    # ects_above_required(current_courses, core, courselist)
    ects_requirements(current_courses, general_1, general_2, techno)