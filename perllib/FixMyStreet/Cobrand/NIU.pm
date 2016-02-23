package FixMyStreet::Cobrand::NIU;
use base 'FixMyStreet::Cobrand::Default';

sub send_questionnaires {
    return 0;
}

sub never_confirm_reports { 1; }

sub allow_anonymous_reports { 1; }

sub anonymous_account { return { name => 'Anonymous Submission', email => FixMyStreet->config('DO_NOT_REPLY_EMAIL') }; }

sub example_places {
    return ( 'Cwmcarn Forest', 'Hyde Park' );
}

sub disambiguate_location {
    return {
        country => 'gb',
        google_country => 'uk',
        bing_culture => 'en-GB',
        bing_country => 'United Kingdom'
    };
}

1;
