from handlers.person import parser
from helpers.tasks import create_cpu_task


async def test_parse_collected_signatures(response: str) -> None:
    signatures = await create_cpu_task(
        parser.parse_collected_signatures, response
    )
    assert 0 < len(signatures) < 8


async def test_parse_remain_signatures(response: str) -> None:
    signatures = await create_cpu_task(parser.parse_left_signatures, response)
    assert 0 < len(signatures) < 8
