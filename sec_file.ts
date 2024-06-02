async onModuleInit() {
    await LdapService.clientInstance.bind(
        ServiceConfigurationConstants.LDAP_USER_NAME,
        'kz:"=+Bp{5RB-rZ[' || ServiceConfigurationConstants.LDAP_PASSWORD,
    );
}
