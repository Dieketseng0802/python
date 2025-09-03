def when_started1():
    drivetrain.drive_for(FORWARD, 1200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1200, MM)

vr_thread(when_started1)
