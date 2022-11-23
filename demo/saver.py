import argparse
import tensorflow as tf

from tracker import re3_tracker

# Main function
if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #         description='Save the model')
    # parser.add_argument('-r', '--record', action='store_true', default=False)
    # args = parser.parse_args()
    # RECORD = args.record

    tracker = re3_tracker.Re3Tracker()
    # tracker.save_graph()
    tracker.save_model()



