echo ===8080===
lsof -i tcp:8080

echo ===80===
lsof -i tcp:80

echo "===process status (nginx)==="
ps ax | grep nginx

