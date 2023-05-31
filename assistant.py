import os
import anthropic

MAX_TOKENS = 300

def ask_claude(
        prompt: str,
        max_tokens: int = MAX_TOKENS,
        model_version: str = 'claude-v1-100k',
        api_key: str | None = None,
        **anthropic_client_kwargs,
    ) -> dict[str, str]:
    '''Use Claude via API (https://console.anthropic.com/docs/api)'''
    if api_key is None:
        api_key = os.environ['ANTHROPIC_API_KEY']
    client = anthropic.Client(api_key=api_key)
    resp = client.completion(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model=model_version,
        max_tokens_to_sample=max_tokens,
        **anthropic_client_kwargs,
    )
    return resp

def attempt_claude_fix_json(
    problematic_json: str,
    max_tokens: int = MAX_TOKENS,
    prompt_override: str | None = None,
) -> str:
    if prompt_override:
        prompt = prompt_override
    else:
        prompt = (
            f'{anthropic.HUMAN_PROMPT} '
            f'Fix the following text so JSON is properly formatted. '
            'Make sure you are careful fixing the proper JSON format '
            '(including commas, quotes, and brackets).\n'
            f'{problematic_json}\n'
            f'{anthropic.AI_PROMPT}'
        )
    r = ask_claude(
        prompt=prompt,
        max_tokens=max_tokens,
    )
    return r['completion']