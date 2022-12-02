ln -sf $(dirname -- "$(realpath -- $0;)";)/dashboardentropia /etc/nginx/sites-enabled/dashboardentropia
sudo systemctl restart nginx.service