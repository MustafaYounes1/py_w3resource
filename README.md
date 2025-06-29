# w3resource Python Exercises
Welcome to my repository of Python exercises, showcasing solutions to an extensive array of problems sourced from 
[w3resource](https://www.w3resource.com/python-exercises/?source=post_page-----ce7e5074e79d--------------------------------).

Spanning beginner to advanced levels, these exercises provide a robust platform for sharpening Python programming skills 
through hands-on practice. The solutions are carefully organized for seamless navigation and quick reference, making this 
a valuable resource for learners and developers alike.

```
001_basic_01............................... 150        002_basic_02............................... 150        003_basic_python_programming_puzzles....... 100        
004_basic_mastering_python................. 100        005_condition_statements_and_loops.........  44        006_recursion..............................  11        
007_python_data_types_str.................. 113        008_python_data_types_json.................   9        009_python_data_types_list................. 280        
010_python_data_types_list_advanced........  15        011_python_data_types_dict.................  80        012_python_data_types_tuple................  33        
013_python_data_types_set..................  29        014_python_data_types_collections..........  36        015_python_data_types_array................  24        
016_python_data_types_enum.................   5        017_python_class...........................  28        018_python_concepts_unittest...............  10        
019_python_concepts_exception_handling.....  10        020_python_concepts_oop....................  10        021_python_concepts_decorator..............  11        
022_functional_programming_functions.......  21        023_functional_programming_lambda..........  51        024_functional_programming_map.............  17        
025_functional_programming_itertools.......  42        026_functional_programming_filter..........  11        027_date_and_time_datetime.................  60        
028_file_handling_file_io..................  20        029_file_handling_file_csv.................  11        030_regular_expressions....................  56        
031_DSA_sort_and_search....................  32        032_DSA_linked_list........................  10        033_DSA_binary_search_tree.................   5        
034_DSA_heap_queue.........................  21        035_DSA_bisect.............................   8        036_advanced_data_types_boolean............  10        
037_advanced_data_types_None...............  10        038_advanced_data_types_bytes_and_bytearray  10        039_advanced_data_types_memoryview.........   7        
040_advanced_data_types_frozenset..........   7        041_advanced_data_types_namedtuple.........   9        042_advanced_data_types_ordereddict........  10        
043_advanced_data_types_counter............   8        044_advanced_data_types_ellipsis...........   6        045_concurrency_threading..................   7        
046_concurrency_asynchronous_io............   8        047_miscellaneous_generators...............  17        

....................................................................Total exercises: 1,722...................................................................
```

## Getting started
To begin exploring this repository, follow these straightforward steps:

### 1. Clone the Repository
```
git clone https://github.com/MustafaYounes1/py_w3resource
cd py_w3resource
```

### 2. Set Up Your Environment

#### Python installation
 * Ensure Python >= 3.11 is installed on your system.
 * run: `pip install -r requirements.txt`
     
#### Conda installation
  * Install Miniconda, Miniforge, or Anaconda.
  * run: `conda env create -f conda_env_win.yml` (Windows)

## Practice on random exercises
Elevate your Python proficiency by tackling random exercises using the CLI of `exercise.py`. This utility enables you to 
fetch and solve exercises on demand, with customizable options for exercise quantity, source categories, and reproducibility: 

```
usage: exercise.py [-h] [-n NUM_EXERCISES] [-src SOURCES [SOURCES ...]]
                   [-s SEED]

Practice and improve your skills by solving randomized exercises using this tool.

options:
  -h, --help            show this help message and exit
  -n NUM_EXERCISES, --num_exercises NUM_EXERCISES
                        Number of random exercises to fetch. (default: 1)
  -src SOURCES [SOURCES ...], --sources SOURCES [SOURCES ...]
                        Source groups from which the random exercises would be fetched. 
                        By default, all subdirectories present in the current file directory would be considered as source groups. (default: YOUR_PATH_TO/py_w3resource)
  -s SEED, --seed SEED  Seed optional argument for reproducibility. (default: None)
```

## Add more exercises
Contribute to the repository by adding your own exercises with these guidelines:

* Create a dedicated Python script for each new exercise.
* Document the exercise problem in the script’s docstring.
* Group related exercises in a subdirectory, naming each script with its exercise ID.

Streamline this process with the `create_template_scripts.py` CLI tool:

``` 
usage: create_template_scripts.py [-h] first_exc_id last_exc_id out_dir

A tool to automate the creation of multiple template scripts for multiple w3resource exercises, where each script name
is the exercise ID and its contents would be the following template:

"""

Describe the task here

"""

def main():
    pass

if __name__ == "__main__":
    main()

positional arguments:
  first_exc_id  The first exercise ID
  last_exc_id   The last exercise ID, must be equal to or greater than 'first_exc_id'
  out_dir       The output directory where the template scripts would be created.

options:
  -h, --help    show this help message and exit
```

Once a group of exercises is complete, consolidate their problem definitions into a `000.txt` file within the group’s 
subdirectory. 

Automate this with the `summarize_exercises.py` tool, This script compiles docstrings from all `.py` files into `000.txt`. 
Note: Each script must include a docstring with the problem definition, ideally created using `create_template_scripts.py` 
for consistency:

```
usage: summarize_exercises.py [-h] group_dir

Use this script to summarize the questions from the exercises' scripts in a certain exercises group that is present
in a dedicated subdirectory.

It would fetch the questions of all exercises (the '*.py' files) and write them down in a text file namely: "000.txt"
that would get created inside the input directory.

Note:   the python scripts are supposed to have a docstring at the beginning that holds the question.
        Best practice would be to create the python scripts with 'create_template_scripts.py'  and then use this
        script to summarize a certain group of exercises.

positional arguments:
  group_dir   The path to the directory that holds the python scripts of the exercises to be summarized.

options:
  -h, --help  show this help message and exit
```
