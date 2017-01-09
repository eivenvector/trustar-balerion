from balerion.TrustarServices import Store
import os

SOURCE_REPORT_DIR = "/Users/nkseib/Downloads/barncat"


def main():
    all_df = []
    store = Store()

    # process all files in directory
    print("Processing and storing each source file in %s" % SOURCE_REPORT_DIR)
    for (dirpath, dirnames, filenames) in os.walk(SOURCE_REPORT_DIR):
        problem_reports = []
        for file_name in filenames:
            print("Processing source file %s " % file_name)
            try:
                path = os.path.join(SOURCE_REPORT_DIR, file_name)
                df = store.process_file(path)
                store.store_file(df)
                if type(df) == str:
                    print "None Not Allowed"
                else:
                    all_df.append(df)
            except:
                problem_reports.append(file_name)
                print("Problem with file %s, exception: " % file_name)
                continue


if __name__ == '__main__':
    main()