import requests



def get_transcripts():
    transcript_urls = ['https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s3/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s2/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s4/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s5/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s6/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s7/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s8/allwords_clean.txt',
'https://raw.githubusercontent.com/serapoint/rupaul-subtitles-analysis/master/subtitles/s9/allwords_clean.txt']

    for transcript in transcript_urls:
        print(f'{transcript}')
        
get_transcripts()