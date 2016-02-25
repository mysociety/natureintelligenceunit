package FixMyStreet::Cobrand::NIU;
use base 'FixMyStreet::Cobrand::Default';

sub send_questionnaires {
    return 0;
}

sub never_confirm_reports { 1; }

sub allow_anonymous_reports { 1; }

sub anonymous_account { return { name => 'Anonymous Submission', email => FixMyStreet->config('DO_NOT_REPLY_EMAIL') }; }

sub example_places {
    return ( 'Haggerston Park', 'Mile End Park' );
}

sub disambiguate_location {
    return {
        country => 'gb',
        google_country => 'uk',
        bing_culture => 'en-GB',
        bing_country => 'United Kingdom',
        centre => '51.5004698326776,-0.109361505313849',
        span   => '0.40512227589786,0.844407524758742',
        bounds => [ 51.2867018983754, -0.510363135171181, 51.6918241742733, 0.334044389587561 ],
    };
}

sub enter_postcode_text {
    return 'Enter your postcode or area name';
}

sub areas_on_around {
    return [ 144380 ];
}


1;
