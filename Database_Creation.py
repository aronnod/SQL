import pandas as pd
import glob, os
#from sqlalchemy import create_engine

for file in glob.glob("*.csv"):
    df = pd.read_csv(file)
    
    # Create SQLAlchemy engine to connect to MySQL Database
    #engine = create_engine() #not yet set up
                                     
    df.to_sql(file[:-4], engine, index=False)
    
    print('task finished... exiting')

  