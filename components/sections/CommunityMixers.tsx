import Image from 'next/image';
import { Container } from '@/components/site/Container';
import { SectionHeader } from '@/components/site/SectionHeader';
import type { MixersConfig } from '@/lib/content';
import { cn } from '@/lib/utils';

interface Props {
  config: MixersConfig;
}

/**
 * Card tints. Bullet colour is a `bg-*`, so it stays visible against the card
 * rather than inheriting the low-contrast header wash.
 */
const ACCENTS = {
  pink: { header: 'from-pink-400/30 via-orange-300/25 to-yellow-300/20', bullet: 'bg-pink-500' },
  blue: { header: 'from-sky-400/30 via-indigo-400/20 to-purple-400/20', bullet: 'bg-kcd-primary' },
  green: { header: 'from-emerald-400/30 via-teal-300/25 to-cyan-300/20', bullet: 'bg-emerald-600' },
} as const;

/**
 * One card per mixer. A single mixer gets a centred column instead of a
 * stretched third of the row; two or more fall into the grid.
 */
const COLUMNS = ['', 'max-w-xl mx-auto', 'sm:grid-cols-2 max-w-4xl mx-auto', 'sm:grid-cols-2 lg:grid-cols-3'];

export function CommunityMixers({ config }: Props) {
  const { mixers } = config;
  if (mixers.length === 0) {
    return null;
  }

  return (
    <section id="mixers" className="py-20">
      <Container>
        <SectionHeader
          eyebrow={config.eyebrow}
          title={config.title}
          description={config.description}
          align="center"
        />
        <ul className={cn('grid gap-6', COLUMNS[Math.min(mixers.length, 3)])}>
          {mixers.map((m) => {
            const accent = ACCENTS[m.accent];
            return (
              <li key={m.name} className="flex">
                <article className="flex w-full flex-col overflow-hidden rounded-3xl border border-kcd-border bg-white shadow-card">
                  {m.image ? (
                    <div className="relative aspect-[1200/630] w-full bg-kcd-navy">
                      <Image
                        src={m.image}
                        // Art that only restates the heading beside it is
                        // decorative; a real `imageAlt` opts back in.
                        alt={m.imageAlt ?? ''}
                        aria-hidden={m.imageAlt ? undefined : true}
                        fill
                        sizes="(max-width: 640px) 100vw, 576px"
                        className="object-cover"
                      />
                    </div>
                  ) : (
                    <div className={cn('h-24 w-full bg-gradient-to-br', accent.header)} aria-hidden />
                  )}
                  <div className="flex flex-1 flex-col p-6">
                    <h3 className="font-display text-xl font-bold text-kcd-ink">{m.name}</h3>
                    {(m.when || m.where) && (
                      <p className="mt-1 text-sm font-semibold text-kcd-ink/80">
                        {[m.when, m.where].filter(Boolean).join(' · ')}
                      </p>
                    )}
                    {m.description && <p className="mt-2 text-sm text-kcd-ink/75">{m.description}</p>}
                    {m.activities.length > 0 && (
                      <ul className="mt-4 space-y-2 text-sm text-kcd-ink/80">
                        {m.activities.map((a) => (
                          <li key={a} className="flex items-start gap-2">
                            <span
                              className={cn('mt-1.5 inline-block h-1.5 w-1.5 shrink-0 rounded-full', accent.bullet)}
                              aria-hidden
                            />
                            <span>{a}</span>
                          </li>
                        ))}
                      </ul>
                    )}
                    {/* No sign-up of our own: a mixer either links out, says
                        invite only, or says nothing and relies on the footnote. */}
                    {(m.inviteOnly || m.rsvpUrl) && (
                      <div className="mt-6">
                        {m.inviteOnly ? (
                          <span className="inline-flex h-11 items-center justify-center rounded-full border border-kcd-border bg-kcd-subtle px-5 text-xs font-bold uppercase tracking-wider text-kcd-ink/70">
                            Invite only
                          </span>
                        ) : (
                          <a
                            href={m.rsvpUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex h-11 items-center justify-center rounded-full bg-kcd-primary px-5 text-xs font-bold uppercase tracking-wider !text-white"
                          >
                            {m.rsvpLabel}
                            <span className="sr-only"> (opens in a new tab)</span>
                          </a>
                        )}
                      </div>
                    )}
                  </div>
                </article>
              </li>
            );
          })}
        </ul>
        {config.footnote && (
          <p className="mt-8 text-center text-sm text-kcd-ink/70">{config.footnote}</p>
        )}
      </Container>
    </section>
  );
}
