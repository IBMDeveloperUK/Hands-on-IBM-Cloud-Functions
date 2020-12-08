from functools import partial
from pathlib import Path

import ffmpeg

from choirless_lib import create_signed_url


def main(args):

    notification = args.get('notification', {})
    key = args.get('key', notification.get('object_name', ''))

    src_bucket = args['bucket1']
    dst_bucket = args['bucket2']
    
    geo = args['geo']
    host = args.get('endpoint', args.get('ENDPOINT'))
    cos_hmac_keys = args['__bx_creds']['cloud-object-storage']['cos_hmac_keys']
    cos_api_key = cos_hmac_keys['access_key_id']
    cos_api_secret = cos_hmac_keys['secret_access_key']
    
    get_input_url = partial(create_signed_url,
                            host,
                            'GET',
                            cos_api_key,
                            cos_api_secret,
                            geo,
                            src_bucket)
    
    get_output_url = partial(create_signed_url,
                             host,
                             'PUT',
                             cos_api_key,
                             cos_api_secret,
                             geo,
                             dst_bucket)

    output_key = str(Path(key).with_suffix('.wav'))

    stream = ffmpeg.input(get_input_url(key),
                          seekable=0)
    audio = stream.audio
    audio = audio.filter('volumedetect')
    pipeline = ffmpeg.output(audio,
                             get_output_url(output_key))

    cmd = pipeline.compile()
    print("ffmpeg command to run: ", cmd)

    pipeline.run()

    return {'status': 'ok'}

