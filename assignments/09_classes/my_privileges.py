import Admin_privileges
Admin_privileges.first_privilege("host events")
Admin_privileges.second_privilege("and invite users")

from Admin_privileges import first_privilege as fp
fp("host events")