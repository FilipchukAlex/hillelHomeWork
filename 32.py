import os
import csv


#------------------------------------------------------------------------------
def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f, delimiter=';')]
    f.close()

    return list_dicts

#------------------------------------------------------------------------------
def update_students_results(group, hw_results, test1_results, test1_weights):

    for dict_test1_results in test1_results:
        dict_test1_results['task_completion'] = [int(elem) for elem in dict_test1_results['task_completion'][1:-1].split(',')]
        for i, number in enumerate(dict_test1_results['task_completion']):
            for dict_test1_weights in test1_weights:
                if (i + 1) == int(dict_test1_weights['task_id']):
                    dict_test1_results['task_completion'][i] = number  * int(dict_test1_weights['task_weight'])

    for dicts_gr in group:
        for dicts_hw in hw_results:
            for dict_test1_results in test1_results:
                if dicts_gr['id'] == dicts_hw['id'] == dict_test1_results['id']:
                    dicts_gr['rank'] = int(dicts_gr['rank']) + dicts_hw['task_completion'].count('1') + sum(dict_test1_results['task_completion'])

#------------------------------------------------------------------------------
def print_students_info(group, sort_by_key = "fullname"):
    group.sort(key=lambda elem: elem[sort_by_key])
    for dict in group:
        print("-----------------------------------------")
        print("| ID:    %30s |"        % dict['id'])
        print("| Fullname:   %25s |"   % dict['fullname'])
        print("| Email: %30s |"        % dict["email"])
        print("| Github:     %25s |"   % list(reversed(dict["github"].split('/')))[0])
        print("| Rank:  %30s |"        % dict["rank"])
        print("-----------------------------------------")

#------------------------------------------------------------------------------
if __name__ == "__main__":
    group = get_data_from_csv(r'D:\homework\group.csv')
    hw_results = get_data_from_csv(r'D:\homework\hw_results.csv')
    test1_results = get_data_from_csv(r'D:\homework\test1_results.csv')
    test1_weights = get_data_from_csv(r'D:\homework\test1_weights.csv')

    update_students_results(group, hw_results, test1_results, test1_weights)
    print_students_info(group, 'rank')