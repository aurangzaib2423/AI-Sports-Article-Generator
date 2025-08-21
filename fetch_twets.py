{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f6e1311e-ff83-492b-a4e2-2e8a7de00672",
   "metadata": {},
   "outputs": [
    {
     "ename": "TooManyRequests",
     "evalue": "429 Too Many Requests\nUsage cap exceeded: Monthly product cap",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTooManyRequests\u001b[0m                           Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 14\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# --- Fetch latest tweets ---\u001b[39;00m\n\u001b[0;32m     13\u001b[0m query \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#Sports -is:retweet lang:en\u001b[39m\u001b[38;5;124m\"\u001b[39m  \u001b[38;5;66;03m# example hashtag\u001b[39;00m\n\u001b[1;32m---> 14\u001b[0m tweets \u001b[38;5;241m=\u001b[39m client\u001b[38;5;241m.\u001b[39msearch_recent_tweets(query\u001b[38;5;241m=\u001b[39mquery, max_results\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m)\n\u001b[0;32m     16\u001b[0m tweet_texts \u001b[38;5;241m=\u001b[39m [t\u001b[38;5;241m.\u001b[39mtext \u001b[38;5;28;01mfor\u001b[39;00m t \u001b[38;5;129;01min\u001b[39;00m tweets\u001b[38;5;241m.\u001b[39mdata]\n\u001b[0;32m     18\u001b[0m \u001b[38;5;66;03m# --- Save to file ---\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\tweepy\\client.py:1276\u001b[0m, in \u001b[0;36mClient.search_recent_tweets\u001b[1;34m(self, query, user_auth, **params)\u001b[0m\n\u001b[0;32m   1184\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"search_recent_tweets( \\\u001b[39;00m\n\u001b[0;32m   1185\u001b[0m \u001b[38;5;124;03m    query, *, end_time=None, expansions=None, max_results=None, \\\u001b[39;00m\n\u001b[0;32m   1186\u001b[0m \u001b[38;5;124;03m    media_fields=None, next_token=None, place_fields=None, \\\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1273\u001b[0m \u001b[38;5;124;03m.. _Academic Research Project: https://developer.twitter.com/en/docs/projects\u001b[39;00m\n\u001b[0;32m   1274\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m   1275\u001b[0m params[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mquery\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m query\n\u001b[1;32m-> 1276\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_request(\n\u001b[0;32m   1277\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGET\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/2/tweets/search/recent\u001b[39m\u001b[38;5;124m\"\u001b[39m, params\u001b[38;5;241m=\u001b[39mparams,\n\u001b[0;32m   1278\u001b[0m     endpoint_parameters\u001b[38;5;241m=\u001b[39m(\n\u001b[0;32m   1279\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mend_time\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexpansions\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmax_results\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmedia.fields\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1280\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnext_token\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mplace.fields\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpoll.fields\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mquery\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1281\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msince_id\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msort_order\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstart_time\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtweet.fields\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   1282\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muntil_id\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muser.fields\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1283\u001b[0m     ), data_type\u001b[38;5;241m=\u001b[39mTweet, user_auth\u001b[38;5;241m=\u001b[39muser_auth\n\u001b[0;32m   1284\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\tweepy\\client.py:129\u001b[0m, in \u001b[0;36mBaseClient._make_request\u001b[1;34m(self, method, route, params, endpoint_parameters, json, data_type, user_auth)\u001b[0m\n\u001b[0;32m    123\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m_make_request\u001b[39m(\n\u001b[0;32m    124\u001b[0m     \u001b[38;5;28mself\u001b[39m, method, route, params\u001b[38;5;241m=\u001b[39m{}, endpoint_parameters\u001b[38;5;241m=\u001b[39m(), json\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[0;32m    125\u001b[0m     data_type\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, user_auth\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m    126\u001b[0m ):\n\u001b[0;32m    127\u001b[0m     request_params \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_process_params(params, endpoint_parameters)\n\u001b[1;32m--> 129\u001b[0m     response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mrequest(method, route, params\u001b[38;5;241m=\u001b[39mrequest_params,\n\u001b[0;32m    130\u001b[0m                             json\u001b[38;5;241m=\u001b[39mjson, user_auth\u001b[38;5;241m=\u001b[39muser_auth)\n\u001b[0;32m    132\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mreturn_type \u001b[38;5;129;01mis\u001b[39;00m requests\u001b[38;5;241m.\u001b[39mResponse:\n\u001b[0;32m    133\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\tweepy\\client.py:115\u001b[0m, in \u001b[0;36mBaseClient.request\u001b[1;34m(self, method, route, params, json, user_auth)\u001b[0m\n\u001b[0;32m    113\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mrequest(method, route, params, json, user_auth)\n\u001b[0;32m    114\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m--> 115\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m TooManyRequests(response)\n\u001b[0;32m    116\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mstatus_code \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m500\u001b[39m:\n\u001b[0;32m    117\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m TwitterServerError(response)\n",
      "\u001b[1;31mTooManyRequests\u001b[0m: 429 Too Many Requests\nUsage cap exceeded: Monthly product cap"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import tweepy\n",
    "from dotenv import load_dotenv\n",
    "\n",
    "# --- Load environment variables ---\n",
    "load_dotenv(\"a.env\")  # your .env file\n",
    "BEARER_TOKEN = os.getenv(\"BEARER_TOKEN\")\n",
    "\n",
    "# --- Twitter Client ---\n",
    "client = tweepy.Client(bearer_token=BEARER_TOKEN)\n",
    "\n",
    "# --- Fetch latest tweets ---\n",
    "query = \"#Sports -is:retweet lang:en\"  # example hashtag\n",
    "tweets = client.search_recent_tweets(query=query, max_results=10)\n",
    "\n",
    "tweet_texts = [t.text for t in tweets.data]\n",
    "\n",
    "# --- Save to file ---\n",
    "with open(\"sample_tweets.txt\", \"w\", encoding=\"utf-8\") as f:\n",
    "    for t in tweet_texts:\n",
    "        f.write(t + \"\\n\")\n",
    "\n",
    "print(\"✅ Latest tweets saved to sample_tweets.txt\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9600f664-a7c8-43a5-8564-a93d0f4a4974",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
