import sys
import os
import datetime
import json
import wget

def main():
    if len(sys.argv) != 3:
        print 'Usage: query_api logfilename outfilename'
        exit(1)
    logfilename = sys.argv[1]
    call = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?sort=newest&fq=source%3A%22The+New+York+Times%22+AND+document_type%3A%22article%22&api-key=8cbd506758608f03f71e955c07315a98%3A4%3A69419709'
    wget.download(call,out=logfilename)
    json_file = open(logfilename)
    json_data = json.load(json_file)
    json_file.close()
    os.remove(logfilename)
    
    outfile = open(sys.argv[2], 'a')
    if len(json_data['response']['docs']) == 0:
        outfile.write( '{0}: No documents received!\n'.format(datetime.datetime.now()) )
    else:
        article = json_data['response']['docs'][0]
        outfile.write( '{2}: The most recent article published on NYTimes.com is "{1}", publication date {0}\n'.format(article['pub_date'], article['headline']['main'], datetime.datetime.now()) )
    outfile.close()

if __name__ == '__main__':
    main()