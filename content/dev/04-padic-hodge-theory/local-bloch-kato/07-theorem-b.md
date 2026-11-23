---
title: Theorem B
decls:
  - GlobalTheory.T.theoremB_of_localFilteredHypotheses
  - GlobalTheory.theoremB_of_admitted_inputs
  - GlobalTheory.T.localLiftingTheoremB_of_blochKato_tateDuality_eulerChar
  - GlobalTheory.theoremB_closing
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem B

Theorem B bounds the congruence length of a surjective map $F : T_1 \to T_2$ of crystalline lattices in Case A, when the Hodge-Tate weights of $T_1$ at each letter lie in a short window around a size. The bound is linear in the number of letters and in the rank of $T_2$, with a constant $C \ge 320$. This section proves Theorem B from the admitted statements of Section 6 and three further inputs, and then for the local data of the series. The result is used in [the inert step](/entry/inert-step-main-alt-alt/).

We keep the notation of Section 6. Fix a prime $\ell$ and finite extensions $K$, $L$ of $\mathbb{Q}_\ell$, with $\mathcal{O}$ the ring of integers of $L$ and $K_0$ the maximal unramified subfield of $K$. For a lattice $T$ write $Z^1_f(T)$ for the module of finite cocycles of $T$ (the cocycles whose class lies in $H^1_f$) and $B^1(T)$ for the coboundaries. A *lattice map* $F : T_1 \to T_2$ is an $L$-linear map of the spaces, compatible with the action of $G_K$, continuous, with $F(T_1) \subseteq T_2$.

**Definition 7.7.1 (Congruence length).** Let $F : T_1 \to T_2$ be a lattice map and put $I(F) = F_* Z^1_f(T_1) + B^1(T_2)$. The *congruence length* of $F$ is the length of the $\mathcal{O}$-module
$$\mathrm{col}(F) = \mathrm{length}_{\mathcal{O}}\, Z^1_f(T_2) / \big(I(F) \cap Z^1_f(T_2)\big).$$
For a real $x$ we say that $\mathrm{col}(F) \le x$ *relative to $\ell$* if $\mathrm{col}(F)$ and $e = \mathrm{length}_{\mathcal{O}}(\mathcal{O}/\ell)$ are finite and $\mathrm{col}(F) \le x\, e$. For $e' \ge 0$, $F$ *lifts with exponent $e'$* if $\ell^{e'} z \in I(F)$ for every $z \in Z^1_f(T_2)$.

**Definition 7.7.2 (Hida setting).** Let $n$ be the number of letters of the Wach data at $(K, L)$, and let $b, w, S, \eta, m \ge 0$, a sign $\mathrm{up}(i) \in \{\text{true}, \text{false}\}$ and a size $\mathrm{size}(i) \ge 0$ for each letter $i$, and two further functions $M_i$, $h_i$ of the letters. A letter $i$ is *thick* if $b \le \mathrm{size}(i) \le b + \eta$. A lattice map $F : T_1 \to T_2$ is in the *Hida setting* for these data if:

1. $(K, L)$ is in Case A;
2. $T_1$ and $T_2$ are crystalline and $F$ is surjective;
3. $\eta < \mathrm{size}(i)$ for every letter $i$;
4. at every letter $i$ and every embedding $\tau$ over $\tau_i$, the jumps of $T_1$ lie in $[\mathrm{size}(i), \mathrm{size}(i) + S] \cup [-\eta, \eta]$ if $\mathrm{up}(i)$ is true, and in $[-\mathrm{size}(i) - S, -\mathrm{size}(i)] \cup [-\eta, \eta]$ if not;
5. at every letter $i$, the number of jumps of $T_2$ in $[-\eta, \eta]$, counted with multiplicity over all $\tau$ over $\tau_i$, is at most $m$;
6. every letter that is not thick has size at most $w$;
7. the jumps of $T_1$ are bounded at each letter by $M_i$ and $h_i$, in a form that we do not unfold.

Put $h = b + \eta + S$ if some letter is thick and $h = w + S$ if not, and $\lambda = \log_\ell(2h)$. The *band condition* for a constant $C$ is that some letter $i$ that is not thick has a thick neighbour $i \pm 1$ and satisfies
$$|\ell\, \mathrm{size}(i) - b| \le C\big(\ell\eta + \ell S + b/\ell + \mathrm{size}(i) + \ell\lambda\big).$$
Put $\beta = 1$ if the band condition holds and $\beta = 0$ if not. The *lifting exponent* is $e' = 2\epsilon_W + \epsilon_U$, where, for maxima $M$ and $H$ built from $M_i$ and $h_i$ and a finite set $J$ of jumps of $T_1$,
$$\epsilon_W = \Big\lfloor \frac{H\ell}{(\ell-1)^2} + 3 + \log_\ell(H+1) \Big\rfloor, \qquad \epsilon_U = \sum_{j \in J} v_\ell(j) + a + v_\ell(a!), \qquad a = \Big\lfloor \frac{M}{\ell - 1} \Big\rfloor + 1.$$
We do not unfold $M$, $H$ and $J$.

**Definition 7.7.3 (Theorem B at $(K, L)$).** *Theorem B with constant $C$* at $(K, L)$ is the statement: let $\ell \ge 11$ and let $F : T_1 \to T_2$ be in the Hida setting, with $20w \le b$, $20\eta \le b$, $20S \le b$, and some letter not thick. Let $r$ be the dimension over $L$ of the space of $T_2$. Then:

1. if $\mathrm{up}(i + 1) \ne \mathrm{up}(i)$ for every $i$ and no three consecutive letters are thick, then, relative to $\ell$,
$$\mathrm{col}(F) \le C(n+1)r\Big(\frac{h}{\ell^2} + \frac{w + \eta}{\ell} + S + 1 + \lambda + \eta\beta\Big) + Cnme';$$
2. if $R \ge 1$, $\mathrm{up}$ is constant and no $R$ consecutive letters are thick, then, relative to $\ell$,
$$\mathrm{col}(F) \le C(n+1)r\Big(\frac{h}{\ell^2} + \frac{w + \eta}{\ell} + R^2(S + 1 + \lambda) + \eta\beta\Big) + CnmR^2 e'.$$

*Theorem B with constant $C$* for local data is Theorem B at every $(K, L)$ in Case A with $K$ inside the maximal unramified extension of $\mathbb{Q}_\ell$, for the Wach data of $H_\ell$ at $(K, L)$.

Theorem B from the admitted statements needs three more inputs. *Fontaine's inequality* says $\dim_L D_{\mathrm{cris}}(V) \le [K_0 : \mathbb{Q}_\ell] \dim_L V$ for every finite-dimensional representation $V$ of $G_K$ over $L$; $V$ is crystalline when equality holds. The *jump statement* says: for an exact sequence $0 \to T_0 \to T_1 \to T_2 \to 0$ of crystalline lattices and an embedding $\tau$, an integer $a$ is a jump of $T_1$ at $\tau$ if and only if it is a jump of $T_0$ or of $T_2$ at $\tau$; here $a$ is a jump if $\mathrm{Fil}^{a+1} \ne \mathrm{Fil}^a$. The *letter condition* is a statement about the Wach module of a crystalline lattice in Case A at a letter $i$: if $\ell^y z$ lies in the $\Delta$-invariant part, then so does $\prod_{x \in X} (\delta - c(x)) z$, where $\delta$ is the operator with $\pi_0 \delta z = \gamma z - z$, $-\ell c(x) = \chi(\gamma)^{-x} - 1$, and $X$ is a finite set that contains $a + j$ for each jump $a$ at $i$ and $1 \le j \le y$.

**Theorem 7.7.4 (Theorem B from the admitted statements).** Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. Let $C_0 \ge 320$, and assume Fontaine's inequality, the jump statement and the letter condition for the local data. Then, for all constants $(C_R, C_A, C_B, C_K, C_\kappa)$, if the admitted statements of Theorem B hold, Theorem B with constant $C_0$ holds for the local data.

Lean: `GlobalTheory.T.theoremB_of_localFilteredHypotheses` (also `GlobalTheory.theoremB_of_admitted_inputs`).

*Proof.* Fix $\ell \ge 11$, $(K, L)$ and $F : T_1 \to T_2$ as in Theorem B. The number of letters is $n = [K_0 : \mathbb{Q}_\ell]$. The admitted statements give two facts on $T_2$ and $F$. First, the bound on generators of $H^1_f$ gives $g$ elements that generate the image of $Z^1_f(T_2)$ in cohomology. Second, a part of the last of the local lifting statements shows that $F$ lifts with exponent $e'$. A counting lemma says: if $Z$ is a finite set of finite cocycles of $T_2$ and $\ell^{e_0}$ times every finite cocycle lies in $I(F)$ plus the span of $Z$, then $\mathrm{col}(F) \le g e_0 + |Z| e'$ relative to $\ell$. So it is enough to find $e_0$ and $Z$.

Put $\Sigma = h/\ell^2 + (w + S + \eta)/\ell + \lambda + 1$. In the alternating case there are two subcases. If some letter is thick and $b/4 < 40\Sigma$, the Wach module arguments show that $F$ lifts with an exponent $e_0 \le 160\Sigma$, and $Z$ is empty. In the other subcase they give $e_0 \le 55\Sigma + 13S + \eta\beta$ and a set $Z$ with $|Z| \le 4nm$. In the constant case they give $e_0 \le 18\Sigma + 3R^2(S + 1 + \lambda) + 1$ and a set $Z$ with $|Z| \le (R + 1)nm$. These arguments use the admitted statements, the inputs on jumps and filtrations, and the letter condition. A computation with $C_0 \ge 320$ then turns $g e_0 + |Z| e'$ into the bounds of Theorem B. $\square$

**Theorem 7.7.5 (Theorem B for the local data).** Assume the theorem of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. Then Theorem B with constant $C_0$ holds for the local data for every $C_0 \ge 320$.

Lean: `GlobalTheory.T.localLiftingTheoremB_of_blochKato_tateDuality_eulerChar` (also `GlobalTheory.theoremB_closing`).

*Proof.* Fontaine's inequality holds for the local data, and the jump statement follows from the tie: for crystalline lattices in an exact sequence the jumps of the middle term are those of the ends. [The clauses on Wach lattices](/entry/wach-lattice-later-clauses-hold/) give a norm bound on $\Delta$-invariant lattices, and the letter condition follows from it. [The hypotheses of Theorem B](/entry/local-lifting-theorem-b-hypotheses-admitted/) give the admitted statements with $(10, 23, 32, 32, 8)$. Now apply [Theorem B from the admitted statements](/entry/theorem-b-of-local-filtered-hypotheses/). $\square$

**Remark 7.7.6 (Formalization).** The three published inputs enter only through the hypotheses of Theorem B, where they are not used (Section 6), so the theorem holds without them. Of the admitted statements, the proof uses only parts of the first statement and statements 2 to 4, two of the five killer statements, and statements 6 to 12 ([AdmBoundsBOfAdm.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/AdmBoundsBOfAdm.lean#L87)); the inequality $\kappa(C_\kappa)$ and the Bloch-Kato extension criterion are not used. Clause 1 of Theorem B is empty when $n$ is odd, since a sign that changes at every step of $\mathbb{Z}/n$ needs $n$ even. The jump statement exists in two files with the same body ([LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L650)), and one lemma proves both. The Hida setting has no Hida family in it. The two main Lean names are one-line wrappers that set `maxHeartbeats` to 1000000.
