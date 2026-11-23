---
title: The colength bound from frames
decls:
  - Formalism.MainNotions.N.Ln34.integrality_from_metric_of_large_constant
  - Formalism.MainNotions.N.Ln34.lifting_theorem_of_uniform_link
  - Formalism.MainNotions.N.Ln34.frame_pf
  - Formalism.MainNotions.N.Ln34.framepf_rec
  - Formalism.MainNotions.N.Ln34.u1link_pf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The colength bound from frames

This section proves a second bound on the colength of a map of lattices that is onto, for every constant $C \ge 160$. Here $K$ may be ramified over $K_0$, with $(K, L)$ good at level $1$, and each embedding $\tau \colon K \to L$ carries its own window of jumps. The proof reduces the bound to three facts on finite cocycles. The third, a killing exponent, uses a pair of maps between two modules attached to a cut, a *frame*. We prove that frames exist, and that a frame splits the image of an invariant vector into a part with known coordinates and a part of small rank. The bound is used in [the local colength bound for $160 \le C$](/entry/integrality-from-metric-of-le/).

We keep the notation of [the local Theorem B](/entry/thm-b-at/) and of [Wach data](/entry/theorem-of-literature-hypotheses/): the prime $p$, the fields $K_0 \subseteq K$ with $n = [K_0 : \mathbb{Q}_p]$, the letters $i \in \mathbb{Z}/n$, the ring $\Lambda$ with idempotents $e_i$, and for a lattice $T$ the module $D(T)$, the Wach module $N(T)$ and the module $N_i(T)$ of $\Delta$-invariant vectors in the letter $i$. Put $e = [K : K_0]$. For $b, S \in \mathbb{N}$ let $W^{\uparrow}(b, S) = [b, b + S]$ and $W^{\downarrow}(b, S) = [-b - S, -b]$.

**Definition 8.16.1 (Setting of the colength bound).** Let $F \colon T_1 \to T_2$ be a map of lattices, $r, S, \eta, m, h \in \mathbb{N}$, and for each embedding $\tau \colon K \to L$ a sign $\mathrm{up}_\tau$ and a size $b_\tau \in \mathbb{N}$. Write $W_\tau = W^{\uparrow}(b_\tau, S)$ if $\mathrm{up}_\tau$ holds and $W_\tau = W^{\downarrow}(b_\tau, S)$ otherwise. We are in the *setting of the colength bound* if:

1. $T_1$ and $T_2$ are crystalline, $F$ is onto, and $\dim_L V_2 = r$;
2. for each $\tau$ the jumps of $T_1$ at $\tau$ lie in $W_\tau \cup [-\eta, \eta]$, and $\eta < b_\tau$;
3. for each $\tau$ the multiplicities of the jumps of $T_2$ at $\tau$ in $[-\eta, \eta]$ add up to at most $m$;
4. the jumps of $T_1$ lie in $[-h, h]$;
5. $e = 2$, or $\mathrm{up}_\tau$ depends only on $\tau|_{K_0}$.

For $C \in \mathbb{R}$ put
$$B(C) = C (ne + 1)\, r \Bigl( \frac{eh}{p} + eS + e \log_p h + 1 + \eta \Bigr) + n e (e + 1)\, m\, C (h + 1).$$
The *colength bound with constant* $C$ holds if, for every prime $p \ne 2$, every pair $(K, L)$ good at level $1$ and every datum in the setting of the colength bound, $\operatorname{col}(F) \le B(C) \cdot \lambda$.

**Definition 8.16.2 (Hypotheses of the colength bound).** The *admitted conditions* are thirteen statements at every prime: the existence of $\Delta$-invariant Wach lattices, Herr classes and their naturality, the lifting theorem in all cases with constants $C_A, C_B, C_K$, statements on Wach modules, the bound on generators of finite classes, $\dim D_{\mathrm{cris}}(V) \le n \dim V$ and $\dim D_{\mathrm{dR},\tau} \le \dim V$, additivity of multiplicities in short exact sequences, and restriction to finite extensions. The three *side hypotheses* are:

1. the Wach functor $T \mapsto D(T)$ takes a short exact sequence of lattices to an exact sequence;
2. $\dim_L D_{\mathrm{dR},\tau}(V) = \dim_L V$ for each crystalline $V$ and each $\tau$;
3. for each crystalline $T$ and each letter $c$, the image of the Wach module at $c$ in $D_{\mathrm{cris}}(V)$ has dimension $\dim_L V$.

**Definition 8.16.3 (Frame at a cut).** Fix $h' \ge 1$ and a letter $c$. Assume $\pi' \in \Lambda^\Delta$ and polynomials $P_i$ of degree $e$ satisfy the *ring relations*: every $a \in \Lambda^\Delta$ is, letter by letter, a unique power series in $\pi'$, $\pi'$ is a unit times a power of the uniformizer of $\Lambda$, and with $\epsilon = (P_i(\pi'_i))_i$ we have $q = u_1 \epsilon$, $\varphi(\pi') = u_2 \pi' \epsilon^{s}$ and $\gamma(\pi') - \pi' = u_3 \pi' \epsilon$ for units $u_1, u_2, u_3$, where $s = (p - 1)/e$. Put
$$M = \Bigl\lceil \frac{4h'}{s} \Bigr\rceil, \qquad \sigma = M - 1 + v_p\bigl((M - 1)!\bigr).$$
For a lattice $T$ let $\bar N_{c-1}(T) = N_{c-1}(T) / (N_{c-1}(T) \cap \pi' N(T))$. Let $\mathcal{L}_c(T)$ be the set of $x \in E \otimes_{\mathcal{O}} \bar N_{c-1}(T)$ with $\epsilon^{h'} x$ in the image of $e_c \Lambda^\Delta \otimes \bar N_{c-1}(T)$, and let $\mathcal{P}_c(T)$ be the set of $\Delta$-invariant $y \in e_c D(T)$ with $\epsilon^{h'} y$ in the span of $\varphi(N_{c-1}(T))$. Each has a submodule $J$, the image of $\pi'^M \epsilon^{3h'}$ times the corresponding integral module. A *frame* at $c$ is a pair of families of $\mathcal{O}$-linear maps
$$\alpha_T \colon \mathcal{L}_c(T) \to \mathcal{P}_c(T)/J, \qquad \beta_T \colon \mathcal{P}_c(T) \to \mathcal{L}_c(T)/J$$
such that, for every crystalline $T$ with jumps in $[-h', h']$: $\alpha_T$ and $\beta_T$ kill $J$; $\beta_T \alpha_T$ and $\alpha_T \beta_T$ are multiplication by $p^{2\sigma}$; both commute with $\Lambda^\Delta$ and with $\gamma$; the levels at $c$ of a lift of $\alpha_T(x)$ are $p^\sigma$ times a product series built from a representation of $x$; and both are natural in maps of crystalline lattices.

So a frame identifies the two modules up to $J$ and up to the factor $p^{2\sigma}$.

**Proposition 8.16.4 (Frames exist).** Assume the existence of $\Delta$-invariant Wach lattices. Let $p \ne 2$, $(K, L)$ good at level $1$, and $\pi'$, $P$ satisfying the ring relations. Then for each $h' \ge 1$ and each letter $c$ there is a frame at $c$ with $M$ and $\sigma$ as above.

Lean: `Formalism.MainNotions.N.Ln34.frame_pf` (also `Formalism.MainNotions.N.Ln34.framepf_rec`)

*Proof.* Since the level is $1$ and $p \ne 2$, the element $\gamma_K$ of the Wach datum is $\gamma$. We have $s \ge 1$, and $M \ge 4h'/s$ gives $4h' \le sM$, so $M \ge 1$. From $\varphi(\pi') = u_2 \pi' \epsilon^s$ and $4h' \le sM$ we get $\varphi(\pi')^M = \pi'^M \epsilon^{4h'} u$ with $u \in \Lambda^\Delta$. The ring relations also give $\gamma(\pi') = \pi' f$, $\gamma(\epsilon) = \epsilon t$ and $\epsilon = \gamma(\epsilon) t'$ with $f, t, t' \in \Lambda^\Delta$, and $\pi'$ and $\epsilon$ are units in $E$.

It suffices to give, for each crystalline $T$, maps $h_T \colon \bar N_{c-1}(T) \to D(T)$, $\Psi_T \colon E \otimes \bar N_{c-1}(T) \to D(T)$ and $\Phi_T$ in the other direction, with $\Psi_T(\mathcal{L}_c) \subseteq \mathcal{P}_c$, $\Phi_T(\mathcal{P}_c) \subseteq \mathcal{L}_c$, and:

1. $\gamma h_T(z) - h_T(z) \in \pi'^M N(T)$, and $h_T(\bar z) - p^\sigma z \in \pi' N(T)$;
2. $\Psi_T(a \otimes z) = a\, \varphi(h_T(z))$;
3. $\Psi_T$ and $\Phi_T$ preserve $J$, and $\Phi_T \Psi_T - p^{2\sigma}$ and $\Psi_T \Phi_T - p^{2\sigma}$ map into $J$;
4. $p^{2\sigma} x \in J$ forces $x \in J$ on $\mathcal{L}_c$, and for $x \in \pi' N(T)$ invariant under $\Delta$, $\gamma x - x \in \pi'^M N(T)$ forces $x \in \pi'^M N(T)$;
5. the level condition of a frame.

Then $\alpha_T = \Psi_T \bmod J$ and $\beta_T = \Phi_T \bmod J$ form a frame; on lattices that are not crystalline we take the zero maps.

These maps come from a basis $b_1, \dots, b_r$ of $N(T)$ over $\Lambda$ made of $\Delta$-invariant vectors, such that $\Delta$-invariant vectors have coordinates in $\Lambda^\Delta$, together with a power series $F_s$ with $\gamma_0(\pi'_{c-1}) = \pi'_{c-1} F_s(\pi'_{c-1})$, constant term $\chi_\Gamma(\gamma)^s$, $\chi_\Gamma(\gamma)^{sy} \ne 1$ for $y \ge 1$, and
$$p^\sigma = a_\sigma \prod_{y=1}^{M-1} \bigl( \chi_\Gamma(\gamma)^{sy} - 1 \bigr)$$
for some $a_\sigma \in \mathcal{O}$. The admitted existence of $\Delta$-invariant Wach lattices gives these data. In the basis, $\Psi_T$ is given by a matrix $H$ over $\mathcal{O}[[X]]$, read in $\pi'_{c-1}$ and moved by $\varphi$. The map $\Phi_T$ comes from a second matrix: if $H' H = \lambda + X^M K_1$ and $H H' = \lambda + X^M K_2$ with $\lambda \in \mathcal{O}$, there is $\Phi$ that preserves $J$, maps $\mathcal{P}_c$ into $\mathcal{L}_c$, and has $\Phi \Psi_H - \lambda$ and $\Psi_H \Phi - \lambda$ with values in $J$. $\square$

**Definition 8.16.5 (First frame proposition).** Let $\alpha, \beta$ be a frame at $c$, and let $F \colon T_1 \to T_2$, $S, \eta, m, h'$, $\mathrm{up}$, $b$ satisfy: $T_1, T_2$ crystalline, $F$ onto, the jumps of both lattices at $\tau$ in $W_\tau \cup [-\eta, \eta]$, $\eta < b_\tau$, $b_\tau + S \le h'$, $h' \ge 1$, the multiplicity condition 3 for $T_2$, and condition 5. Let $\Omega$ be the set of $i \in [-h', h']$ such that for some $\tau$ over $c$ either $\mathrm{up}_\tau$ holds and $-b_\tau - S \le i < -b_\tau$, or $\mathrm{up}_\tau$ fails and $b_\tau \le i < b_\tau + S$. Put $\pi_\Omega = \prod_{i \in \Omega} (1 - u^i)$, with $u$ the unit of the Wach datum. The *first frame proposition* holds for $\beta$ if there are a submodule $L_r \subseteq \bar N_{c-1}(T_2)$ of rank at most $e m$ and $\ell_1, \dots, \ell_k \in N_{c-1}(T_2)$ such that:

1. $\ell_j$ lies in the filtration step $b_\tau$ at every $\tau$ over $c$ with $\mathrm{up}_\tau$;
2. the classes of the $\ell_j$ and $L_r$ span $\bar N_{c-1}(T_2)$;
3. for each $\gamma$-invariant vector $w$ of $\mathcal{P}_c(T_2)$ modulo $\pi'$, there are coordinates $f_j \in E$, $x \in \mathcal{L}_c(T_2)$ and $x_r$ invariant over $L_r$ with $\beta(\pi_\Omega w) = [x]$ and $x - \sum_j f_j \otimes \ell_j - x_r \in \pi' \mathcal{N}$, where $\mathcal{N}$ is the span of the filtered vectors of $\mathcal{L}_c(T_2)$.

A *coordinate* $f$ satisfies $\epsilon^{h'} f = a \in e_c \Lambda^\Delta$, the levels of $a$ vanish below $h' - b_\tau$ at up embeddings and are proportional to those of $\epsilon^{h'}$ below $h' + b_\tau + S$ at down embeddings, and $\epsilon^{h'}(\gamma f - f) \in \pi' \Lambda^\Delta$.

So the image of $w$ splits into a part with controlled coordinates and a part of rank at most $em$.

**Theorem 8.16.6 (First frame proposition).** Assume the existence of $\Delta$-invariant Wach lattices and side hypotheses 2 and 3, and assume the models of the levels of $\mathcal{L}_c$ and of the filtration on it. Then the first frame proposition holds for every frame, at every $p \ne 2$, every $(K, L)$ good at level $1$ and every $\pi'$, $P$ with the ring relations.

Lean: `Formalism.MainNotions.N.Ln34.u1link_pf`

*Proof.* Since $\eta < b_\tau$ and $b_\tau + S \le h'$, the window $W_\tau \cup [-\eta, \eta]$ lies in $[-h', h']$, so the jumps of $T_2$ lie in $[-h', h']$. The models then apply to $T_2$ at $c$. The ring relations give $\epsilon, \pi' \in \Lambda^\Delta$, both units in $E$, $\gamma(\epsilon) = u_E \epsilon$ with $u_E$ invertible in $\Lambda^\Delta$, and $\gamma(\pi') = \pi' u_\pi$. At each point over $c$ the level of $\epsilon$ has constant term $0$ and nonzero linear term, the level of $\pi'$ has nonzero constant term, and $\gamma$ acts on levels by rescaling with $u$. There are at most $e$ embeddings $\tau$ over $c$. The module $\bar N_{c-1}(T_2)$ has a basis with representatives in $N_{c-1}(T_2)$, and the value maps at the points over $c$ are additive, $\mathcal{O}$-linear and agree at points over the same $\tau$.

Side hypotheses 2 and 3 control the filtration: at an up embedding, a combination of the basis in the step $-i$ with $i < -(b_\tau + S)$ is $0$, and the step $b_\tau$ has codimension at most $m$; at a down embedding the step $-b_\tau + 1$ has dimension at most $m$, and everything lies in the step $-(b_\tau + S)$. A general lemma on frames turns these facts into the first frame proposition. $\square$

**Theorem 8.16.7 (Colength bound from the first frame proposition).** Assume the first frame proposition for every frame. Let $C \ge 160$, assume the three side hypotheses, and let $C_A, C_B, C_K \in \mathbb{R}$. Then the admitted conditions imply the colength bound with constant $C$.

Lean: `Formalism.MainNotions.N.Ln34.lifting_theorem_of_uniform_link`

*Proof.* At each $p \ne 2$ and $(K, L)$ good at level $1$, and for each datum in the setting, it suffices to prove three facts:

1. there are at most $g = 2(ne + 1) r$ finite cocycles that span $Z^1_f(T_2)$ modulo $B^1(T_2)$;
2. $F$ lifts with exponent $e' = 2(4h + v_p((4h)!)) + \sum_{j \in J}(1 + v_p(j)) + h + v_p(h!)$ for a set $J \subseteq [-h, 2h]$ with $0 \notin J$;
3. there are $s$ with $es = p - 1$, $h'$ with $1 \le h' \le h + S + 1$, and at most $g_0 = ne(e + 1)m$ finite cocycles $s_0$ with $p^Y Z^1_f(T_2) \subseteq \operatorname{span}(s_0) + \operatorname{Im}_F$, where
$$Y = 2\rho + 4\sigma + \kappa + \max(2\sigma, y), \quad \rho = 2a - 1 + v_p((2a - 1)!), \quad a = \Bigl\lceil \frac{2eh'}{p - 1} \Bigr\rceil,$$
with $\kappa = e(S + v_p(S!) + \lfloor \log_p h' \rfloor)$ and $y = \lceil \eta + 1/2 + \log_p h' \rceil$.

The first two facts are steps proved from the admitted conditions. The third uses most of the steps: the frames, the first frame proposition, the models of levels, the second proposition on ranks, the slot propositions for up, down and mixed letters, and the splitting steps, through a universal step and a killing step. Given the three facts, $\operatorname{col}(F) \le (gY + g_0 e') \lambda$. Next $Y \le 80 (eh/p + eS + e \log_p h + 1 + \eta)$ and $e' \le 18h \le C(h + 1)$. Since $2 \cdot 80 = 160 \le C$, this gives $\operatorname{col}(F) \le B(C) \lambda$. $\square$

**Theorem 8.16.8 (Colength bound for $C \ge 160$).** Let $C \ge 160$ and $C_A, C_B, C_K \in \mathbb{R}$. Assume the three side hypotheses. Then the admitted conditions imply the colength bound with constant $C$.

Lean: `Formalism.MainNotions.N.Ln34.integrality_from_metric_of_large_constant`

*Proof.* Combine the last two theorems. $\square$

**Example 8.16.9.** Let $K = K_0$, so $e = 1$ and $n = [K : \mathbb{Q}_p]$, and let $m = 0$: no jump of $T_2$ lies in $[-\eta, \eta]$. Then condition 5 holds, the second term of $B(C)$ vanishes, and
$$\operatorname{col}(F) \le C (n + 1)\, r \Bigl( \frac{h}{p} + S + \log_p h + 1 + \eta \Bigr) \lambda .$$
Here $g_0 = 0$, so fact 3 says that $p^Y Z^1_f(T_2) \subseteq \operatorname{Im}_F$.

**Remark 8.16.10 (Formalization).** The colength bound with constant $C$ is `Conclusion1 D C`, which is `TheoremBLocal` with `thmA` and `boundA` ([ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L36)); the theorem `integrality_from_metric_of_large_constant` ([MainFinal.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainFinal.lean#L10)) states `IntegralityFromMetric`, which is `Adm1 → Conclusion1` (line 161 there). The name speaks of a metric, but the statement is a colength bound; other files in the folder define other `IntegralityFromMetric` and `Conclusion1`. The proof is `lifting_theorem_of_uniform_link u1link_pf`, and `lifting_theorem_of_uniform_link` ([MainPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainPf.lean#L38)) only passes 28 named steps and its hypothesis to `local_theorem_of_leaf_lemmas`; the "uniform link" of its name is the U1 link `FirstFrameOfModels`. The frame is `IsFrame` and `FrameA`, and the first frame proposition is `FirstPropositionFrame` (DownSlotProposition.lean lines 121, 195 and 216). The step `frame_pf` ([FramePf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/FramePf.lean#L64)) uses only the first conjunct `adm1` of `Adm1`, and calls `framepf_rec` ([FramePfRec.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/FramePfRec.lean#L59)) with `framepf_back` for the matrix inverse. In `framepf_frameA` the frame maps on lattices that are not crystalline are the zero maps (FramePfAsm.lean line 72). The step `u1link_pf` ([U1linkPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/U1linkPf.lean#L16)) reads its facts from the hypothesis by chains of projections and calls `universal_lift_frame`, which binds that hypothesis as `_hHyp` and does not use it (UniversalLiftFrame.lean line 145). All three steps raise `maxHeartbeats` to 1000000. The side hypotheses are `FontExAll`, `DdRFull` and `DiRank`; `FontExAll` and `DiRank` take arguments `_F` and `_Cm` that they do not use.
