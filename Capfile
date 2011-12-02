load 'deploy' if respond_to?(:namespace) # cap2 differentiator
Dir['vendor/plugins/*/recipes/*.rb'].each { |plugin| load(plugin) }


set :application, "xmap"
set :repository,  "git@github.com:LarryEitel/xmap.git"

set :scm, :git
set :use_sudo, false
set :ssh_options, { :user => "www-data", :forward_agent => true }
set :deploy_via, :remote_cache
set :deploy_to, "/srv/x/#{application}"

role :web, "map.xchg.com:53"
role :app, "map.xchg.com:53"
role :db,  "map.xmap.com:53", :primary => true


def django_manage(cmd, options={})
  path = options.delete(:path) || "#{latest_release}"
  run "cd #{path}; ./bin/django #{cmd}"
end

 
namespace :deploy do
  task :finalize_update, :except => { :no_release => true } do
    run "cd #{latest_release}; python bootstrap.py"
    run "cd #{latest_release}; ./bin/buildout -N"
    #django_manage "collectstatic --noinput"
    #django_manage "generatemedia"
    #run "cd #{latest_release}; mv bin/_generated_media_names.py xc"
  end
  task :start do
    run "sudo supervisorctl start #{application}"
  end
  task :stop do
    run "sudo supervisorctl stop #{application}"
  end
  task :restart do
    run "sudo supervisorctl restart #{application}"
  end
  desc "Run manage.py syncdb in latest release."
    task :migrate, :roles => :db, :only => { :primary => true } do
      # FIXME: path, see default railsy deploy:migrate
      m = if fetch(:django_use_south, false) then "--migrate" else "" end
      if fetch(:django_databases, nil)
        fetch(:django_databases, nil).each { |db|
          django_manage "syncdb --noinput #{m} --database=#{db}"
        }
      else
        django_manage "syncdb --noinput #{m}"
      end
    end
end


# set_from_env_or_ask :variable, "Please enter variable name: "
# If there is VARIABLE in enviroment, set :variable to it, otherwise
# ask user for a value
def set_from_env_or_ask(sym, question)
  if ENV.has_key? sym.to_s.upcase then
    set sym, ENV[sym.to_s.upcase]
  else
    set sym do Capistrano::CLI.ui.ask question end
  end
end

  
namespace :django do
  desc <<EOF
Run custom Django management command in latest release.

Pass the management command and arguments in COMMAND="..." variable.
If COMMAND variable is not provided, Capistrano will ask for a command.
EOF
  task :manage do
    set_from_env_or_ask :command, "Enter management command"
    django_manage "#{command}"
  end
end
