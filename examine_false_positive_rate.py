import sys
import subprocess

print('Usage: python examine_false_positive_rate.py [optional_upperlimit: int]')
print("If an keyboard interupt is sent; the gathered data will be outputted.")

upper_limit = None
if len(sys.argv) >= 2:
    upper_limit = int(sys.argv[1])

attempts = 0
false_positives = 0
try:
    while upper_limit is None or attempts <= upper_limit:
        subprocess.run(["bash", "run_demo_test_CKKS.sh"], stdout=subprocess.DEVNULL)
        with open("ckks_32parties_10bits.txt") as result:
            if not ("NOT FOUND in database!" in result.read()):
                false_positives += 1
            attempts += 1
        
                
finally:
    print("Attempts: ", attempts)
    print("False_positives: ", false_positives)