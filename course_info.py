import pandas as pd

def course_importance(course_number: str=None, course_name: str=None) -> None:
    """Use this function to figure out if one specific course is important for getting enough core or
       courselist courses. It should also check if the course is a general competence, technological specialization
       or elective course.
       Input:
            Either a course number of a course name should be input.
        Output:
            No output, but the function prints important info for the studyplan."""




if __name__ == '__main__':
    current_courses = pd.read_csv("current_courses.csv", sep='\t', dtype={0: str, 1: str, 2: str, 3: float})
    core = pd.read_csv("data_science_requirements/core.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})
    courselist = pd.read_csv("data_science_requirements/courselist.csv", sep='\t', dtype={0: str, 1: str, 2: float, 3: str})

    print(core["title"])
    print(core["course_number"])
