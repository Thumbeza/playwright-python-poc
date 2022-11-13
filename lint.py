# import argparse
# import logging
# import sys
# from pylint.lint import Run
#
#
# logging.getLogger().setLevel(logging.INFO)
#
# parser = argparse.ArgumentParser(prog="LINT")
#
# parser.add_argument('-p',
#                     '--path',
#                     help='path to directory you want to run pylint | '
#                          'Default: %(default)s | '
#                          'Type: %(type)s ',
#                     default="./src/main/",
#                     type=str)
#
# parser.add_argument('-t',
#                     '--threshold',
#                     help='score threshold to fail pylint runner | '
#                          'Default: %(default)s | '
#                          'Type: %(type)s ',
#                     default=10.0,
#                     type=float)
#
# args = parser.parse_args()
# PATH = str(args.path)
# threshold = float(args.threshold)
#
# logging.info("PyLint Starting | Path: %s | Threshold: %s", PATH, threshold)
#
# results = Run([PATH], do_exit=False)
#
# final_score: float = results.linter.stats.global_note
#
# if final_score < threshold:
#     message = f"PyLint Failed | Score: {final_score} | Threshold: {threshold}"
#
#     class LintingException(Exception):
#         pass
#
#     logging.error(message)
#     raise LintingException(message)
#
# message = f"PyLint Passed | Score: {final_score} | Threshold: {threshold}"
#
# logging.info(message)
#
# sys.exit(0)
