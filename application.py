import params
import webbrowser
import time

temp_ttw_in_minutes = params.params["time_to_work_in_minutes"]
temp_numb_iteration = params.params["number_of sequences_to_work"]
temp_mibdu_in_minutes = params.params["minor_break_duration_in_minutes"]
temp_mabdu_in_minutes = params.params["major_break_duration_in_minutes"]
is_running = False


def count_down_from(duration):
    duration_in_sec = duration * 60

    while duration_in_sec != 0:
        time.sleep(1)
        duration_in_sec -= 1


while temp_numb_iteration != 0:

    print("Work session #{0}".format(temp_numb_iteration))

    count_down_from(temp_ttw_in_minutes)

    if temp_numb_iteration-1 != 0:
        count_down_from(temp_mibdu_in_minutes)
        webbrowser.open("https://www.youtube.com/watch?v=PhN_ykAYvWQ")

    else:
        print("I am here")
        count_down_from(temp_mabdu_in_minutes)
        webbrowser.open("https://www.youtube.com/watch?v=W_OHqI__nmw")

    temp_numb_iteration -= 1

print("Your work session is over")








