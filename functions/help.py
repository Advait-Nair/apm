from spectrum import col
apmhelp = """
{0}Adva Package Manager
{1}A complete CLI Tool for managing, fetching and updating reusable developer components.{4}

{4}{3}apm about{1} - About apm

{2}FUNCTIONS:{4}

{4}{3}apm vwd or apm{1} - View the component alias statuses in the current working directory.

{4}{3}apm gwd{1} - View the component alias statuses globally.

{4}{3}apm help{1} - prints this help message.

{4}{3}apm load{1} - load a component onto your current directory.

{4}{3}apm unload{1} - unload a component off your current directory.

{4}{3}apm update{1} - Unload & Reload a component, updating it.

{4}{3}apm restoremaster{1} - Restore the last cached version of masterdata.apm.

{4}{3}apm uglify{1} - Compact masterdata.apm, saving space and allowing operations to be performed onto and with it.

{4}{3}apm prettify{1} - Expand masterdata.apm and make it readable.

{4}{3}apm globalunloadall{1} - Unload every component in existence. WARNING! PROJECTS MAY STOP WORKING!

{2}Restore Saved (RSV){4}
{4}{3}apm getrsv{1} - Use a stored manual backup.
{4}{3}apm rsv{1} - Create a custom manual backup.
{4}{3}apm delrsv{1} - Delete a custom manual backup.
{4}{3}apm listrsv{1} - Get all manual backups currently in existence.

{4}{3}apm view{1} - view all installed components.

        -> -ifn: Show In File Name matches with the provided substring, separate each requirement by a whitespace, use multiple -ifn to create "or" ifn conditionals.
        e.g. apm view -ifn .ts -ifn app -rd, list all components with a .ts or app in the filename. Exclude deprecated items. 
        -> -rd: Remove Deprecated from list

""".format(
    col('info-h'), # 0 is title
    col('italic'), # 1 is italic
    col('info'), # 2 is heading
    col('bold'), # 3 is bold
    col('straight') # 4 is normal
)