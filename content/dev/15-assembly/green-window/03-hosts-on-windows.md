---
title: Hosts on windows
decls:
  - UpperTheory.T3.hostOfFieldOf
  - UpperTheory.Top.hostOfField
  - UpperTheory.T3.supplyOfAdmOf
  - UpperTheory.Top.supplyOfAdm
  - UpperTheory.Top.supplyChi
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hosts on windows

This section proves the second input of [ZeroFreeAll from $\mathrm{Top}_G$ and hosts](/entry/zero-free-all-of-top-g/): for each primitive [[Dirichlet character|JR4QSEFXWF]] $\psi$, hosts with the requirement $G_\psi$ exist on windows of scale $\tfrac32$. The input is the window bound [VWin](/step/vwin-def/) at $\psi$. It is the only place where VWin enters [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/). The first theorem completes host axioms to a good host, from two facts on primes. The others build the windows and check the requirement.

We keep the notation of the last section: scales $s$ with size $s.x$, parameter $s.\varepsilon$ and bound $s.b$, ranks $R$ with a frame, hosts, and hosts on windows.

**Definition 3.3.1 (Host axioms and good hosts).** Host axioms $H_0$ on a frame have a modulus $Q_S$, two primes $q$ and $d$, an abelian field $E$, and a map $\mathrm{art}$ on residues. A host $H$ over $H_0$ adds a constant $C_{T2}$, a finite set $T$, two primes $g_0, g_1$, two primes $p, p'$ and further choices. The host is *good* for $(s, C_8, C_5, c_6, C_b, q_0)$ if a list of fourteen conditions holds. Among them: with $N = Q_S q d$, each $g_i = \pi \bar\pi$ for some integer $\pi$ of the field with $\pi \equiv 1 \bmod N$; $p \equiv p' \equiv 1 \bmod \operatorname{lcm}(15, N)$; $q_0$ is a prime with $q_0 \equiv 1 \bmod N$, $q_0 \le N^{C_8}$ and $q_0 \neq p, p'$; and the level primes of $H$ are exactly $g_0, g_1, p, p', q_0$.

Two statements on primes enter. *SmallOne* says: there is $A \ge 1$ such that for each $M \ge 2$ there is a prime $p \equiv 1 \bmod M$ with $p \le M^A$. This follows from Linnik's theorem; see [primes in progressions](/learn/analytic-number-theory/#primes-in-progressions-and-in-short-intervals) in Volume 1. *ShortNorm* is a lower bound for the number of primes $p$ with $4p = A^2 + d B^2$ in an interval $[X, X(1+h)]$, for primes $d \equiv 3 \bmod 4$; see [primes represented by norm forms](/learn/analytic-number-theory/#primes-represented-by-norm-forms).

**Definition 3.3.2 (Statement B).** Statement B says: for each $\varepsilon \in (0, \tfrac{1}{52})$ and $C_0 \ge 1$ there are $C_{T2}$, $C_8 \ge C_0$, $c_6 > 0$, $C_b > 0$ and $x_0$ with this property. Let $s$ be a scale with $s.\varepsilon = \varepsilon$ and $s.x \ge x_0$, let $R$ be ranks with the sizes fixed by $s$, let $H_0$ be host axioms on the frame of $R$, and let $M \in \mathbb{N}$ and $Y \in \mathbb{R}$. Assume:

1. $s.J \le C_0$, $o(R) \le C_0$, $Q_S \le C_0\, n(R)$, $0 < M \le C_0$;
2. $Q_S$ divides $\operatorname{lcm}(2^{e(R)+2}, M)$;
3. $Y$ is a pair window for $s$: $s.x^{1/s.J} \le Y \le s.x$;
4. the pair $(q, d)$ of $H_0$ is good for $(M, \varepsilon, Y, s.x)$, as in [the existence of pairs](/entry/pair-ex/);
5. the field rows of $H_0$ hold up to $\lfloor Y^{\varepsilon/5} \rfloor$, and $R$ is admitted for $H_0$.

Then there are a host $H$ over $H_0$ with constant $C_{T2}$ and a prime $q_0$ such that $H$ is good for $(s, C_8, 4, c_6, C_b, q_0)$, and the set $T$ of $H$ has the shares of the frame up to $s.x^{-1+\varepsilon}$.

**Theorem 3.3.3 (A good host from short norms and small primes).** Assume ShortNorm and SmallOne. Then Statement B holds.

Lean: `UpperTheory.T3.hostOfFieldOf`

*Proof.* Let $N = Q_S q d$ be the conductor of $H_0$. The proof chooses the extra data of $H$ and checks the conditions in groups.

1. SmallOne and ShortNorm give two primes $g_0 \neq g_1$ of size about $(kb)^8$ that are norms $\pi\bar\pi$ with $\pi \equiv 1 \bmod N$, two primes $p, p' \equiv 1 \bmod 15N$ and a prime $q_0 \equiv 1 \bmod N$, all at most $N^{C_8}$. Their splitting in $E$ follows from the congruences.
2. A thick frame lemma gives a second set $T_2$ with no relations, of size between $x^{-\varepsilon} n(R)$ and a fixed fraction of $n_0$.
3. The admission of $R$ for $H_0$ applied to these choices gives a host $D$ over $H_0$.
4. The pair rows give $q, d > 4tr + 1$, the bounds on $q$ and $d$ with constant $4$, and $\log N \le 2 x^{\varepsilon/5} \log^2 x$.
5. A choice of top places gives the set $T$ with the bad set condition and the shares. The host $H$ is $D$ with this $T$.
6. A real box lemma gives the box conditions. Then [the thin host bound](/entry/thin-h/) with $B = C_0$ gives the thin scale condition. The bound on $q$ and $d$ gives $|\mathrm{dlog}(H)| \le 4 \log x \le x^{\varepsilon}$.

$\square$

**Theorem 3.3.4 (A good host for admitted host axioms).** Statement B holds.

Lean: `UpperTheory.Top.hostOfField`

*Proof.* This is the [good host from short norms and small primes](/entry/host-of-field-of/) applied to the proved statements ShortNorm and SmallOne. $\square$

For a primitive $\psi$ of conductor $N_\psi$, host axioms $H_0$ are *cut out by* $\psi$ if $N_\psi \mid Q_S$ and $\mathrm{art}(a) = 1$ exactly when $a \equiv \pm 1 \bmod 2^{e+2}$, $\psi(a) = 1$, and the Jacobi symbols $(a/q)$ and $(a/d)$ are $1$. Write $\mathrm{Adm}_\psi$ for this statement: for each $\varepsilon \in (0, \tfrac{1}{52})$ there is $x_0$ such that for each scale $s$ with $s.\varepsilon = \varepsilon$ and $s.x \ge x_0$, each frame $\varphi$ with $s.x^{2+8\varepsilon} \le \operatorname{ord}(\varphi) \le 2 s.x^{2+8\varepsilon}$ and $o(\varphi) = o(\Lambda_\psi)$, and each host axioms $H_0$ on $\varphi$ cut out by $\psi$, there are ranks $R$ with frame $\varphi$, with the sizes fixed by $s$, and admitted for $H_0$.

**Theorem 3.3.5 (Hosts for one character, given Statement B).** Assume Statement B. Let $\psi$ be a primitive Dirichlet character such that the window bound $\mathrm{VWin}(\psi, 401)$ and $\mathrm{Adm}_\psi$ hold. Then hosts exist on windows of scale $\tfrac32$ with the requirement: $E_{\Lambda_\psi}(H, T, s.x, s.\varepsilon, 4)$ and $V(E_H, R.t, \sqrt{s.b})$.

Lean: `UpperTheory.T3.supplyOfAdmOf`

*Proof.* Fix $\varepsilon$. Let $N$ be the conductor of $\psi$.

1. The existence of good pairs gives windows of scale $\tfrac32$ in which each point $x$ has a window datum: a pair $(q, d)$ good for $(N, \varepsilon, Y, x)$, an exponent $e$ and the bound $V$ with $\lfloor x^{400} \rfloor$. This uses $\mathrm{VWin}(\psi, 401)$.
2. A field lemma for $\psi$ gives frames $\varphi$ of order $c \cdot 2^e$ and host axioms cut out by $\psi$.
3. Apply Statement B with $M = N$ and $C_0 = J + o(\Lambda_\psi) + 8N$, where $J$ comes from the windows. $\mathrm{Adm}_\psi$ gives the ranks.
4. Let $A^{\varepsilon/5} = 5 + 4N$. Take the bound $x_1$ above those of B and of $\mathrm{Adm}_\psi$, and above $A^J$ and $c\,2^{e_0}$. Then $Y \ge A$, so $\lfloor Y^{\varepsilon/5} \rfloor \ge 4N$. Also $q \neq 3$, since $\log q > Y^{\varepsilon/5}/2 > \log 3$, and $e \ge e_0$.
5. $Q_S \le 4Nc\,2^e \le 8N x^{2+8\varepsilon} \le C_0\, n(R)$. Since $Q_S \mid \operatorname{lcm}(2^{e+2}, N)$, each prime factor of $Q_S$ divides $2N$. A lemma on bounded twists then gives the explicit formula conditions with constant $4$.
6. The ranks have $R.t \le x^{400}$ for large $x$, since $\varepsilon < \tfrac{1}{52}$. The bound $V$ is monotone in $t$, so it holds with $t = R.t$.

$\square$

**Theorem 3.3.6 (Hosts for one character from the window bound and admitted ranks).** Let $\psi$ be a primitive Dirichlet character with $\mathrm{VWin}(\psi, 401)$ and $\mathrm{Adm}_\psi$. Then hosts exist on windows of scale $\tfrac32$ with the requirement of the last theorem.

Lean: `UpperTheory.Top.supplyOfAdm`

*Proof.* This is the [hosts for one character, given Statement B](/entry/supply-of-adm-of/) applied to [the good host for admitted host axioms](/entry/host-of-field/). $\square$

**Theorem 3.3.7 (Hosts for one character).** Let $\psi$ be a primitive Dirichlet character with $\mathrm{VWin}(\psi, 401)$. Then hosts with the requirement $G_\psi.\mathrm{req}$ exist on windows of scale $\tfrac32$.

Lean: `UpperTheory.Top.supplyChi`

*Proof.* Apply [the hosts from the window bound and admitted ranks](/entry/supply-of-adm/). Its hypothesis $\mathrm{Adm}_\psi$ follows from a proved lemma on twisted characters: for each scale with $s.x$ large and each frame of the right order there are ranks with the sizes fixed by $s$, and all ranks are admitted for all host axioms. The two conditions $o(\varphi) = o(\Lambda_\psi)$ and "cut out by $\psi$" are not needed. The requirement $G_\psi.\mathrm{req}$ is by definition the requirement of that theorem. $\square$

**Remark 3.3.8 (Formalization).** The theorems are in hostOfFieldOf.lean (line 159), supplyOfAdmOf.lean (line 13), [HostOfField.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean#L8) (lines 8 and 17) and SupplyChi.lean (line 8). The condition "admitted" is always true, by `admissible_ranks_of_CMDatum` (CoprimeRanks/AdmChi.lean line 11), so it carries no content. The constant $C_5$ of a good host is fixed to $4$. The window datum uses the exponent $400$, while VWin uses $401$. In `hostOfFieldOf` the ideal `ccK` of the choices is the unit ideal, so the splitting condition `ccK_split` holds vacuously. The module of `supplyOfAdmOf` is in the folder `ShortNorms`, but its proof uses no short norm statement except through Statement B. Statement B is word for word the statement of `hostOfField`. We have not unfolded `FieldRows`, `PairRow`, `BadOK` or `HostVal`, and we have not opened the proofs of `shortNorm` and `smallOne`.
