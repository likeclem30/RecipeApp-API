import os
os.system("gristle_validator  ../task_data.csv --validschema data/task_data.yml --outgood task_data_good.csv --outerr task_data_err.csv")

os.system("python csv2pgsql.py -f task_data_good.csv -s public  -t task_data -c postgresql://postgres:postgres@localhost/postgres")

