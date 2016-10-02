on run argv
  set ticketNumber to item 1 of input
end run

on getSessionNumber()
	tell application "iTerm"
		tell current session of current window
			set mySession to name
		end tell
	end tell
	if mySession is "Term 1" then
		set badgeID to "user.BADGE"
	else if mySession is "Term 2" then
		set badgeID to "user.BADGE2"
	else if mySession is "Term 3" then
		set badgeID to "user.BADGE3"
	else if mySession is "Term 4" then
		set badgeID to "user.BADGE4"
	end if
end getSessionNumber

on setBadge to ticketNumber
	tell application "iTerm"
		tell current session of current window
			set variable named badgeID to ticketNumber
		end tell
	end tell
	
end setBadge

getSessionNumber
setBadge to ticketNumber
