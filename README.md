# pylearn
Python useful code.

# 1. Androguard

* [Extract strings in methods by python 2 (py2)](https://github.com/ybdesire/pylearn/blob/master/androguard/extract_strings_in_methods.py)


# 2. Network

## 2.1 Google Search API

* [Google search by custom search API (py3)](https://github.com/ybdesire/pylearn/tree/master/google_search_api)


## 2.2 FTP

* [Download file from FTP server (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/ftp_download_files_at_directory.py)
* [Delete file at FTP (py3)](ftplib/del_file_ftp.py)
* [FTP server and client (download/upload) (py3)](https://github.com/ybdesire/WebLearn/tree/master/15_python/pyftpdlib_test)
* [Upload file to specific path at ftp server (py3)](ftplib/ftp_upload_to_path.py)
* [Download file at specific path at ftp server (py3)]( ftplib/ftp_download_from_path.py)
* [list files at ftp dir (py3)](ftplib\ftp_listdir.py)

# 3. Unicode related

* [Fix: UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 2: illegal multibyte sequence (py3)](https://github.com/ybdesire/pylearn/tree/master/unicode_related/open_gbk_file)
* [UTF-8 definition at head (py3)](unicode_related/utf8_head.py)
* [Chinese sub-string find and count (py3)](unicode_related/chinese_string_find_count/chinese_string_find_count.ipynb)

# 4. configparser

* [Install configparser (py3)](https://github.com/ybdesire/pylearn/tree/master/configparser/Readme.md)
* [Read config parameter (py3)](https://github.com/ybdesire/pylearn/tree/master/configparser/read_config)
* [Read config parameter with comment (py3)](https://github.com/ybdesire/pylearn/tree/master/configparser/read_commented_config)


# 5. Template

* [Author & version info (py3)](program_template/init_author.py)
* [Init py file with UTF-8 definition (py3)](unicode_related/utf8_head.py)


# 6. multi-thread

* [Start new thread by threading.Thread.start() (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/multi_thread/1_start_new_thread.py)
* [Start new thread by inherit threading.Thread (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/multi_thread/2_threading_run.py)
* [threading.Lock (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/multi_thread/3_lock.py)
* [threading.Lock with](threading/with_lock.py)
* [threading.RLock](threading/rlock_and_lock.py)
* [Condition wait notify (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/multi_thread/4_condition_wait_notify.py)
* [Event wait and set (py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/multi_thread/5_event_wait_set.py)


# 7. File related
* [list files and dirs at path (py3)](file_related/list_files_at_dir.py)
* [list files and dirs with sub (py3)](file_related/list_files_dirs_sub.py)


# 8. Exception
* [Print exception msg (py3)](exception/ex_print_error.py)
* [Print exception line number (py3)](exception/ex_print_error_line.py)


# 9. Useful tips
* [English punctuations (py3)](string_related/string_punctuation.ipynb)
* [list sort by item (py3)](others/list_sort_by_some_item.py)
* [cut list into sublist chunks(py3)](others/cut_list_into_sublist_chunks.py)
* [format number started with zero(py3)](others/format_with_0x.py)
* [get list from dict sort by value](others/get_list_from_dict_sort_by_value.py)
* [printtolog](others/main_printtolog.py)
* [py program execution time cost](others/py_execution_time_cost.py)
* [Extract email by regx](others/extract_email_from_string.py)
* [process memory usage monitor](others/process_mem_monitor.py)
* [get py module install path](others/get_module_install_path.py)
* [enumerate list with index and value](others/enumerate_list_index_value.py)
* [deep copy](others/deep_copy.py)
* [import failure message](others/import_failure_msg.py)
* [check variable type](others/check_var_type.py)
* [check python 32 or 64 bit](others/check_py_32_64_bit.py)
* [string to dict](others/str_to_dict.py)
* [string strip/trim](others/strip.py)
* [count element occurrences in list](others/py_count_element_occurrences.ipynb)
* [flatten dict: nested dict to none-nested dict](others/flatten_dict.ipynb)
* [get and set system recursion limit](others/recursion_limit.py)
* [math combination problem iteration](others/combinations.py)
* [args kargs](others/py_args_kargs.ipynb)
* [repr to treat \n as 2 characters](others/repr_for_string_escape.py)
* [input a list directly](others/py3_input_a_list_directly.py)
* [sort list of list by length and actual item](others/sort_list_of_list.ipynb)
* [Count number of occurrences of a given substring in a string](others/str_count_substr.py)
* [import module from another path](others/import_module_from_another_path.py)
* [call static methods inside the same class](others/static_method_call_static.py)


# 10. RabbitMQ

* [installation & start service at Win (py3)](rabbitmq/install_rabbitmq_win.md)
* [Send and receive msg(py3)](rabbitmq/send_receive_msg/)
* [Enable and access rabbitmq_management(py3)](rabbitmq/enable_rabbitmq_management.md)
* [Multi-workers(py3)](rabbitmq/work_queues)
* [Publish/Subscribe(py3)](rabbitmq/publish_subscribe)


# 11. Jupyter
* [debug at jupyter](jupyter/jupyter_debug.ipynb)


# 12. Bloom Filter
* [Installation (py2)](pybloom/readme.md)
* [int bloom filter (py2)](pybloom/basic_int.py)
* [string bloom filter (py2)](pybloom/basic_str.py)
* [pybloom  py3 support](https://github.com/jaybaird/python-bloomfilter/issues)


# 13. Multi-Process
* [multi process basic usage(py3)](multi_process/multi_process_basic_usage.py)
* [multi process with parameter(py3)](multi_process/multi_process_with_para.py)
* [process name and id(py3)](multi_process/multi_process_with_name_id.py)
* [multi process timeout](multi_process/multi_process_timeout.py)
* [Ctrl+C / SIGINT and exit multiprocesses](multi_process/multi_process_ctrl_c_end.py)
* [wait all sub process to end](multi_process/wait_all_sub_process.py)


# 14. MySQL(pymysql)
* [Select basic(py3)](https://github.com/ybdesire/WebLearn/blob/master/15_python/mysql_select.py)
* [sql insert](pymysql/insert.py)


# 15. System info
* [memory usage(py3)](system_info/mem_usage.py)
* [get pid(py3)](system_info/pid.py)


# 16. scheduler
* [apscheduler basic](apscheduler/scheduler.ipynb)
* [by linux cmd crontab directly](others/linux_crontab_cmd.md)
* [apscheduler BlockingScheduler](apscheduler/blocking_scheduler.py)
* [apscheduler BackgroundScheduler](apscheduler/background_scheduler.py)
* [apscheduler set max instance](apscheduler/background_max_instances.py)


# 17. pymongo
* [pymongo readme](mongodb/readme.md)
* [mongo connect and find by schema](mongodb/mongo_connect_findone.py)
* [insert_one](mongodb/insert_one.py)
* [remove](mongodb/remove.py)
* [find_one](mongodb/findone.py)
* [find_all](mongodb/find_all.py)
* [find_by_time_period](mongodb/find_by_time_period.py)
* [fuzzy matching](mongodb/fuzzy_match.py)
* [find by multi-values](mongodb/findall_by_multi_values.py)
* [pseudo fuzzy matching](mongodb/pseudo_fuzzy_match.py)
* [update](mongodb/mongo_update.py)
* [check if item exists](mongodb/mongo_check_if_item_exists.py)
* [find string item with non-blank string content](mongodb/mongo_find_non_blank_string.py)
* [find by id,  by _id](mongodb/find_by_id.py)
* [reproduce and fix "RecursionError: maximum recursion depth exceeded in comparison"](mongodb/error_maximum_recursion_depth.py)
* [find by not equal](mongodb/find_by_not_equal.py)


# 18. pywebview
* [web view](pywebview/pywebview.py)


# 19. urllib
* [GET request](urllib/http_get_urllib.py)


# 20. requests
* [GET request](requests/http_get_requests.py)
* [POST request](requests/requests_post.py)
* [time out setting](requests/requests_timeout.py)
* [Acted as Explorer](requests/requests_as_explorer.py)


# 21. package py to exe
* [pyinstaller for simple program at windows](package_exe/pyinstaller/pyinstaller_simple_program)
* [pyinstaller for sklearn program at windows](package_exe/pyinstaller/pyinstaller_with_sklearn)
* [pyinstaller for ubuntu](package_exe/pyinstaller/pyinstaller_ubuntu)
* [run packaged elf file and get output by python](package_exe/pyinstaller/pyinstaller_ubuntu/test.py)


# 22. logging
* [index](logging/)
* [logging basic usage](logging/basic_usage.py)
* [display error only](logging/show_error_only.py)
* [log format](logging/log_format.py)
* [log to file](logging/log_to_file.py)
* [log to file and console](logging/log_to_file_and_console.py)
* [log to multi files rotation](logging/log_to_multi_files_rotation.py)


# 23. json
* [convert dict to json](json/dict_to_json.py)
* [dump json to file with readable format](json/json_to_file.py)
* [load json from file](json/read_from_file.py)


# 24. C langauge extending
* [py call C with basic parameter at linux](py_call_c_language/basic_py_call_c_linux)
* [py call C with basic parameter at win](py_call_c_language/basic_py_call_c_win)


# 25. Cython
* [basic demo](cython/basic_demo/readme.md)


# 26. time
* [get file creation time](time/get_file_create_time.py)
* [add or minus month by datetime](time/add_or_minus_month.py)
* [construct datetime from string](time/construct_datetime_from_string.py)
* [get datetime year/month/day](time/get_datetime_year_month_day.py)
* [add or minus year/month/day](time/time_add_substract_hms.py)
* [get seconds of two time substraction](time/get_seconds_of_two_time_substraction.py)
* [datetime to string](time/datetime_to_string.py)


# 27. BeautifulSoup
* [basic operation](BeautifulSoup/b4_baisc.py)
* [find all specific tag](BeautifulSoup/b4_find_tag_all.py)
* [find all specific tag with multi-properties](BeautifulSoup/b4_find_tag_all_multi_prop.py)
* [with real http requests](BeautifulSoup/b4_real_requests.py)


# 28. Cryptology
* [RSA encrypt/decrypt](cryptology/rsa_encrypt_decrypt.py)
* [base64 encoding]( cryptology/base64_encoding.py)
* [base64 decode](cryptology/base64_decode.py)



# 29. WebSocket
* [basic concept](websocket/Readme.md)
* [server/client code](websocket/basic_server_client)


# 30. deuces(py2)
* [deuces basic](deuces/basic_usage.py)
* [generate random cards](deuces/generate_random_cards.py)
* [evaluate cards rank by score](deuces/evaluate_cards_score.py)
* [evaluate cards rank by class](deuces/evaluate_cards_rank_class.py)
* [strategy example](deuces/basic_strategy.py)
* [evaluate than 5 cards](deuces/evaluate_cards_score_than5.py)
* [texas holdem strategy example](deuces/stratege_input_card_output_action.py)


# 31. gym
* [readme](gym/readme.md)
* [no ai game](gym/no_ai_gym.py)
* [CartPole env details](gym/cart_pole_init_details.py)
* [CartPole observation,action,reward,done details](gym/cart_pole_more_details.py)
* [MountainCar-v0 details](gym/mountain_car_more_details.py)
* [more gym env & examples](https://gym.openai.com/envs/)


# 32. ast
* [how to install](ast/readme.md)
* [convert string representation of list to list](ast/literal_eval.py)


# 33. math
* [floor & ceil](math/floor_ceil.py)


# 34. zmq
* [zmq server](zmq/basic/zmq_client.py)
* [zmq client](zmq/basic/zmq_server.py)


# 35. langdetect
* [detect language of string](langdetect/language_detect.py)


# 36. flask_restful
* [RESTful API by flask_restful](flask_restful/rest_server.py)
* [add sklearn model in flask_restful](flask_restful/rest_server_with_ai.py)
* [RESTful API by flask_restful with CORS](flask_restful/rest_server_cors.py)
* [simple http server with front end](flask_restful/simple_http_server_with_front_end)


# 37. socketio
* [what is socketio](socketio/basic/what.md)
* [socketio basic demo](socketio/basic/readme.md)


# 38. pynpt
* [keyboard listener](pynpt/keyboard_listener.py)


# 39. tkinter
* [basic gui](tkinter/basic.py)
* [capture user input](tkinter/capture_user_input.py)
* [layout adjust](tkinter/layout.py)
* [check button](tkinter/check_button.py)
* [file browser](tkinter/browser_btn.py)
* [complex example](tkinter/complex_example.py)


# 40. xml
* [parse xml basic by xml.etree.ElementTree](xml/parse_xml_basic.py)
* [find element and get element text](xml/find_element.py)
* [find attribute and get attribute text](xml/find_attri.py)


# 41. DataStructure
* [list as stack](datastructure/list_stack.py)
* [list as queue](datastructure/list_queue.py)
* [link list simple implementation](datastructure/link_list.py)
* [tree simple implementation](datastructure/tree.py)


# 42. Pendulum
* [get China time](Pendulum/basic.py)
* [get valid timezon](Pendulum/get_valid_timezons.py)


# 43. termcolor
* [termcolor basic: print colored text](termcolor/termcolor-basic.ipynb)


# 44. redis
* [install and start redis at linux](redis/install_linux.md)
* [python redis basic](redis/basic_connect.py)
* [check redis memory usage](redis/memory_usage.py)


# 45. pathlib
* [basc usage/replace os.path.join]( pathlib/basic.py )


# 46. collections
* [OrderedDict](collections/ordered_dict.py)
* [defaultdict](collections/defaultdict.py)
* [namedtuple](collections/namedtuple.py)
* [deque](collections/deque.py)


# 47. sympy
* [sympy basic usage](sympy/basic_intro.ipynb)
* [simplify expression](sympy/simplify.py)


# 48. itertools
* [multi list combination](itertools/multi_list_combination_by_itertools.ipynb)
* [logic source code of multi list combination/itertools product](itertools/multi_list_combination_logic_source_code.ipynb)


# 49. mmap
* [basic mmap read/write](mmap/mmp_r_w.py)
* [parse bin file by byte accessing](mmap/byte_access.py)


# 50. struct
* [parse bytes to long int](struct/parse_bytes_to_long_int.py)
* [parse byte string by big/little endian](struct/byte_str_to_big_little_endian.py)


# 51. traceback
* [traceback basic exception enhancement](traceback/traceback_basic.py)


# 52. uiautomator
* [setup android auto ui test environment](uiautomator/readme.md)


# 53. re
* [extract strings from string with special bracket format](re/extract_str_from_str_with_bracket.py)
* [re.match(), match re with list of strings](re/match.py)


# 54. objsize
* [get list/dict size in memory as byte](objsize/get_object_size.ipynb)


# 55. elasticsearch
* [count elasticsearch](elasticsearch/count.py)


# 56. inspect
* [get module,package source code](inspect/get_module_package_source_code.py)


# 57. reloadr
* [hot update, auto reload modified module](reloadr/)


# 58. os
* [fork, getpid, get parent id](os/osfork.py)


# 59. talib
* [talib environment setup](talib/env_setup.md)
* [simple moving average](talib/sma.py)


# 60. timeout-decorator
* [basic timeout demo by sigal](timeout-decorator/timeoutdemo.py)
* [set timeout by process](timeout-decorator/tmot_byp.py)


# 61. argparse
* [arg parse basic](argparse/argbasic.py)

# 62. psutil
* [check if process exists by name](psutil/check_if_process_exists_by_name.py)
* [get all running process cmdline](psutil/get_all_running_process_cmdline.py)
* [get all running process name](psutil/get_all_running_process_name.py)
* [kill process by pid](psutil/kill_process_by_pid.py)


# 63 celery
* [worker & sender basic](celery/worker_sender_test/readme.md)


