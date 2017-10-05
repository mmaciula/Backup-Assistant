# Backup-Assistant

# User manual:

  1. To use Backup Assistant you need a Google Drive client. Thanks to Petter Rasmussen you can download Google Drive CLI Client from `https://github.com/prasmussen/gdrive` .
  2. Put the downloaded `gdrive` file into `gdrive_bin` directory.
  3. Run `chmod +x` to make binary executable.
  4. The first time `gdrive` is launched, run `gdrive abou`t in your terminal instead of just gdrive to get a verification code.
  5. Config the `config.json` file by setting the environment variables. `gdrive_dir_id` is a destination folder id from your Google Drive account. `gdrive_bin` is a type of your downloaded client.
  
  
  Default clean time is one week.
