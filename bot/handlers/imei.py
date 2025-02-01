from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject
from fluent.runtime import FluentLocalization
from utils.imei_api import check_imei

router = Router()


@router.message(CommandStart())
async def cmd_start(
        message: Message,
        l10n: FluentLocalization,
):
    await message.answer(
        l10n.format_value("cmd-start"),
        parse_mode=None,
    )


@router.message(Command("check_imei"))
async def cmd_donate(
        message: Message,
        command: CommandObject,
        l10n: FluentLocalization,
):
    if command.args is None:
        await message.answer(l10n.format_value("imei-args-required"))
        return
    if not (8 <= len(command.args) <= 15):
        await message.answer(l10n.format_value("imei-args-rule"))
        return
    imei_number = command.args
    res_imea = check_imei(imei_number)
    if 'error' in res_imea.keys():
        if res_imea["error"] == '405 Server Error':
            await message.answer(
                l10n.format_value("imei-server-error")
            )
            return
        elif res_imea["error"] == '422 Validation Error':
            await message.answer(
                l10n.format_value("imei-validation-error")
            )
            return
    await message.answer(
      l10n.format_value('imei-result').format(deviceName=res_imea['properties']['deviceName'])
    )
    return
