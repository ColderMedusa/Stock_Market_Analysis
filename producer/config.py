import logging
import os

from dotenv import load_dotenv 

load_dotenv()

#configure logging
logging.basicConfig(
    filename='stock_data_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


BASEURL = "alpha-vantage.p.rapidapi.com" # URL for the Alpha Vantage API on RapidAPI to extract the data from the API and send it to the Kafka topic.

url = f"https://{BASEURL}/query" 

api_key = os.getenv('API_KEY')

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": BASEURL
}