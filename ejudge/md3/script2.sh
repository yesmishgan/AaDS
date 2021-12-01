RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
for i in {1..102};
do 
cat "tests/testsB/Input/${i}.txt" | python3 richman.py > out.txt
RESULT=$(diff out.txt tests/testsB/Output/${i}.txt)
#echo "tests/testsB/Input/${i}.txt"
#echo "tests/testsB/Output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "${GREEN}[PASSED]${NC} TEST ${i}"
else
    echo "${RED}[FAILED]${NC} TEST ${i}"
fi;
done
