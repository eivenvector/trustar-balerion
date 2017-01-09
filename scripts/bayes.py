from owl.TrustarServices import Metrics
import argparse
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    print __name__
    return "Welcome to TruSTAR Owl!"


@app.route("/query")
def query():
    return query_barncat('1.2.3.4')


def query_barncat(indicator):
    metrics = Metrics()
    malwares = metrics.get_class_values('MALWARE')

    x = indicator
    n = metrics.get_records_number()

    print 'Total number of records is {}.\n'.format(n)
    print '#################################'
    print 'Computing probabilities of malwares {} for indicator {}.\n'.format(malwares, x)
    print '#################################'
    print 'Malware Frequencies:\n'
    n_y = metrics.get_class_distribution('MALWARE')
    print json.dumps(n_y, indent=2)

    print '#################################'
    n_x = metrics.get_indicator_frequency(x)
    print 'Frequency of occurrence of indicator {}: {}.'.format(x, n_x)
    print '#################################'
    print 'Frequency of co-occurrence of malwares with indicator {}:\n'.format(x)

    n_x_y = metrics.get_indicator_class_frequency(x, malwares)
    print json.dumps(n_x_y, indent=2)
    print '#################################'
    print 'Compute odds of malwares for indicator {} for a uniform prior:\n'.format(x)

    p_u_i = metrics.get_uniform_odds(n_x_y, n_y)
    print json.dumps(p_u_i, indent=2)
    print '#################################'
    print 'Compute odds of malwares for indicator {} for a non-uniform prior:\n'.format(x)

    p_n_i = metrics.get_non_uniform_odds(n_x_y)
    print json.dumps(p_n_i, indent=2)


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=('Query barncat data using an indicator and returns probabilities of '
                                                  'different RAT types\n'
                                                  'Example:\n\n'
                                                  'python bayes.py -i f34d5f2d4577ed6d9ceec516c1f5a744'))
    parser.add_argument('-i', '--indicator', required=True, dest='indicator', help='input indicator')

    # Indicator
    args = parser.parse_args()
    indicator = args.indicator

    query_barncat(indicator)


if __name__ == '__main__':
    app.run()
    # main()
