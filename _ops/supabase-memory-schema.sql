-- Claude Code memory layer — schema for Locate Digital agency
-- Project: qjknsfutbcobxropixud.supabase.co
-- Apply via Supabase Dashboard → SQL Editor → New query → paste → Run
-- Safe to re-run (uses IF NOT EXISTS).

-- ============================================================
-- 1. session_memories — one row per /wrapup
-- ============================================================
create table if not exists public.session_memories (
  id uuid primary key default gen_random_uuid(),
  session_date date not null,
  project_path text not null,
  project_name text not null,
  summary text not null,
  actions_taken text[] not null default '{}',
  decisions_made text[] not null default '{}',
  rules_learned text[] not null default '{}',
  pending_items text[] not null default '{}',
  data_discovered text[] not null default '{}',
  problems_and_solutions text[] not null default '{}',
  created_at timestamptz not null default now()
);

create index if not exists session_memories_project_path_idx
  on public.session_memories (project_path);
create index if not exists session_memories_session_date_idx
  on public.session_memories (session_date desc);

-- ============================================================
-- 2. projects — one row per ongoing project / client
-- ============================================================
create table if not exists public.projects (
  id uuid primary key default gen_random_uuid(),
  project_key text not null unique,
  project_name text not null,
  project_path text,
  context text,
  pending_items text[] not null default '{}',
  category_data jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists projects_project_key_idx
  on public.projects (project_key);

-- Auto-touch updated_at on PATCH
create or replace function public.touch_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists projects_touch_updated_at on public.projects;
create trigger projects_touch_updated_at
  before update on public.projects
  for each row execute function public.touch_updated_at();

-- ============================================================
-- 3. global_rules — cross-project feedback / patterns / references
-- ============================================================
create table if not exists public.global_rules (
  id uuid primary key default gen_random_uuid(),
  rule_key text not null unique,
  category text not null check (category in ('feedback', 'pattern', 'reference')),
  content text not null,
  created_at timestamptz not null default now()
);

create index if not exists global_rules_category_idx
  on public.global_rules (category);

-- ============================================================
-- 4. RLS — lock down so only service role can read/write
-- ============================================================
-- Service role bypasses RLS automatically, so the wrapup/startup
-- skills (which use SUPABASE_SERVICE_ROLE_KEY) keep working.
-- Anon key is denied — these tables hold private agency context.
alter table public.session_memories enable row level security;
alter table public.projects          enable row level security;
alter table public.global_rules      enable row level security;
