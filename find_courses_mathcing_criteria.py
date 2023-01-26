import pandas as pd
from typing import List
import numpy as np


def _in_title(course_title: str, df):
    """Check if the course title is in the given dataframe"""
    return course_title in list(df["title"])


def find_potential_courses(current_courses, core, courselist, general_1, general_2, techno, requirements: List[str]) -> None:
    """Use this function to figure out if one specific course is important for getting enough core or
       courselist courses. It should also check if the course is a general competence, technological specialization
       or elective course.
       Input:
            Either a course number of a course name should be input.
        Output:
            No output, but the function prints important info for the studyplan."""
    for title, time in zip(core.title, core.timetable_group):
        print(time, title, sep="    ")

    for title in current_courses.title:
        get_conditionals = {"course": _in_title(title, courselist),
                            "core": _in_title(title, core),
                            "general": _in_title(title, general_1) or _in_title(title, general_2),
                            "techno": _in_title(title, techno),
                            "elective": not (_in_title(title, general_1) or _in_title(title, general_2)) and not (_in_title(title, techno))}
        print(np.all([get_conditionals[requirement] for requirement in requirements]), title, sep="      ")


if __name__ == '__main__':
    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})

    # Load courses for certificate
    core = pd.read_csv("data_science_requirements/core.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    courselist = pd.read_csv("data_science_requirements/courselist.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    # Load courses for categories
    general_1 = pd.read_csv("master_requirements/general_competence_1.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    general_2 = pd.read_csv("master_requirements/general_competence_2.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    techno = pd.read_csv("master_requirements/technological_specialization.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    req = ["course", "core", "techno"]
    find_potential_courses(current_courses, core, courselist, general_1, general_2, techno, req)
