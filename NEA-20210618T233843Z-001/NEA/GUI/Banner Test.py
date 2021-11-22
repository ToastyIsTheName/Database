def print_banner(root):
    log.info(r"---------------------------------------------------------------")
    log.info(r"                                    _                  __      ")
    log.info(r"   _  ______  _____      ____ ___  (_)___ __________ _/ /____  ")
    log.info(r"  | |/_/ __ \/ ___/_____/ __ `__ \/ / __ `/ ___/ __ `/ __/ _ \ ")
    log.info(r" _>  </ /_/ (__  )_____/ / / / / / / /_/ / /  / /_/ / /_/  __/ ")
    log.info(r"/_/|_|\____/____/     /_/ /_/ /_/_/\__, /_/   \__,_/\__/\___/  ")
    log.info(r"                                  /____/                       ")
    log.info(r"---------------------------------------------------------------")
    log.debug("CORD repo root", root=root)
    log.debug("Storing logs in: %s" % os.environ["LOG_FILE"])
    log.debug(r"---------------------------------------------------------------") 