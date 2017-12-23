import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'ACCOUNT',
    group: true,
  },
  {
    title: 'Logout',
    icon: 'ion-android-person',
    link: '/pages/login',
  },
  {
    title: 'ANALYTICS',
    group: true,
  },
   {
    title: 'Overview',
    icon: 'ion-android-globe',
    link: '/pages/overview',
  },
  {
    title: 'Performance',
    icon: 'ion-heart',
    link: '/pages/performance',
  },
  {
    title: 'Recommendations',
    icon: 'ion-person-stalker',
    link: '/pages/recommendations',
  },
  {
    title: 'Trending',
    icon: 'ion-arrow-graph-up-right',
    link: '/pages/trending',
  },
];
