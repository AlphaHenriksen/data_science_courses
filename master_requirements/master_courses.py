import pandas as pd
import matplotlib.pyplot as plt

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


def ects_requirements(current_courses, general_1, general_2, techno):
    """Undersøger om der er taget for få eller for mange kurser i teknologiske linjefag eller generelle kompetencer"""

    general_1_commons = pd.merge(current_courses, general_1["title"], how='inner')
    general_2_commons = pd.merge(current_courses, general_2["title"], how='inner')
    techno_commons = pd.merge(current_courses, techno["title"], how='inner')
    names = ["entrepreneurship", "general competance", "technological specialization", "thesis"]

    print(f"Total courses taken from {names[0]}: ")
    print(general_1_commons, "\n")
    print(f"Total courses taken from {names[1]}: ")
    print(general_2_commons, "\n\n")
    print(f"Total courses taken from {names[2]}: ")
    print(techno_commons, "\n\n")
    print(f"Total courses taken from {names[3]}: ")
    print(current_courses[current_courses.title == "Master's Thesis"], "\n\n")
    totals = [sum(general_1_commons["points"]),
              sum(general_2_commons["points"]),
              sum(techno_commons["points"]),
              current_courses.points[current_courses.title == "Master's Thesis"].values[0]]
    neededs = [10, 20, 30, 30]

    for (name, total) in zip(names, totals):
        print(f"Points from {name}: {total}")
    print()

    for (total, needed, name) in zip(totals, neededs, names):
        if total >= needed:
            print(f"The requirements for {name} have been satisfied")
    print()

    print(f"The total number of ECTS points in the plan is {sum(current_courses.points) - 10}\n")  # Subtract 10 from total since these points are from the bachelor

    plt.bar(list(range(len(totals)-1)), [totals[0] + totals[1], totals[2], totals[3]], color=["red", "purple", "orange"])
    plt.axhline(30, color="k", linestyle="--")
    plt.show()


if __name__ == '__main__':

    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})
    general_1 = pd.read_csv("master_requirements/general_competence_1.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    general_2 = pd.read_csv("master_requirements/general_competence_2.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    techno = pd.read_csv("master_requirements/technological_specialization.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    # print(general_1)
    ects_requirements(current_courses, general_1, general_2, techno)
