FROM jbarciauskas/xblock-sdk
RUN mkdir -p /usr/local/src/xblock-quote-of-the-day
VOLUME ["/usr/local/src/xblock-quote-of-the-day"]
RUN echo "pip install -e /usr/local/src/xblock-quote-of-the-day" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "exec python /usr/local/src/xblock-sdk/manage.py \"\$@\"" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN chmod +x /usr/local/src/xblock-sdk/install_and_run_xblock.sh
ENTRYPOINT ["/bin/bash", "/usr/local/src/xblock-sdk/install_and_run_xblock.sh"]
CMD ["runserver", "0.0.0.0:8000"]
