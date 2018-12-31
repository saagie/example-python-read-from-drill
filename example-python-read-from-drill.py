from pydrill.client import PyDrill

# ====== Connection ======
# Connecting to drill by providing a drillbit ip and the drill rest api port (31000 by default)
conn = PyDrill(host=os.environ['IP_DRILLBIT'], port=os.environ['DRILL_API_PORT'])

# ====== Reading files ======
# The file employee.json is installed with drill as an example sample
query = conn.query('SELECT * FROM cp.`employee.json` LIMIT 20', timeout=60)

# Create a pandas DataFrame with the result of the query
df = query.to_dataframe()
