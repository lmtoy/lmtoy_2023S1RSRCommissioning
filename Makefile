


include PID 

help:
	@echo PID=$(PID)
	@echo WORK_LMT=$(WORK_LMT)
	@echo "Targets here:"
	@echo "   runs      - make the run1/run2/... files"
	@echo "   summary   - update the project summary index"


# echo $(lmtinfo.py grep 2022 Science 2021-S1-US-3|awk '{print $2}')


runs:
	./mk_runs.py

#          maintain the needed symlinks of the comments.txt file
comments:
	@for p in $(PID); do \
	(echo $$p &&  c=`pwd` &&  cd $(WORK_LMT)/$$p && rm -f comments.txt && ln -s $$c/comments.txt); \
	done

summary:
	@for p in $(PID); do \
	(echo $$p;  cd $(WORK_LMT)/$$p; mk_summary1.sh > README.html); \
	done
