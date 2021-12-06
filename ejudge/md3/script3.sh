RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
for i in {1..22};
do 
cat "tests/testsC/Input/${i}.txt" | python3 bloom.py > out.txt
RESULT=$(diff out.txt tests/testsC/Output/${i}.txt)
#echo "tests/testsC/Input/${i}.txt"
#echo "tests/testsC/Output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "${GREEN}[PASSED]${NC} TEST ${i}"
else
    echo "${RED}[FAILED]${NC} TEST ${i}"
fi;
done
