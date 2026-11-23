---
title: Theorem E in lifting form
decls:
  - Formalism.MainNotions.WachCoordinates.Br.crystalline_lifting_second_form
  - Formalism.MainNotions.WachCoordinates.Br.realised_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem E in lifting form

Theorem E bounds the exponent with which a map of crystalline lattices that is onto lifts finite classes, when the jumps of the source lie in windows of the [kinds of letters](/entry/split-case-a-final/) and the letters are cut into arcs. This section states it for one ordering of the letters and proves it from a list of hypotheses on a Wach datum. The proof moves the lattices into coordinates over $\mathcal{O}[[X]]$, where [the final form of Theorem E](/entry/theorem-e-final-form/) applies, and the arc data come from [the realisation of the arc data](/entry/realised2-pf/). The result is used in [the local lifting theorem from local inputs](/entry/local-theorem-of-inputs/).

We keep the [period datum, lattices, maps of lattices and jumps](/entry/thm-b-at/) of the first section, and the Wach datum $W$ at $(p, K, L)$ with its ordering $\mathrm{emb}$ of the letters. A lattice $T$ in $V$ has *good coefficients* if $L$ is finite over $\mathbb{Q}_p$ with exactly $[K : \mathbb{Q}_p]$ embeddings $K \to L$ over $\mathbb{Q}_p$, $V$ carries the module topology over $L$, and $\mathcal{O}$ is a discrete valuation ring with fraction field $L$.

**Definition 8.5.1 (Letter conditions).** Let $\mathrm{emb} \colon \mathbb{Z}/n \to \mathrm{Hom}_{\mathbb{Q}_p}(K_0, L)$. The *letter conditions* hold for $(\mathrm{emb}, v)$ if $K_0 \to K$ is a bijection, $L$ is finite over $\mathbb{Q}_p$, $n = [K_0 : \mathbb{Q}_p]$, $\mathrm{emb}$ is a bijection with $\mathrm{emb}_{i+1} \circ \sigma = \mathrm{emb}_i$, and $v(p) = 1$.

**Definition 8.5.2 (Cuts and conditions on the kinds).** Let $\mathrm{ty}$ give each letter a kind: thin, up of size $b$, or down of size $b$. Let $j \ge 1$, let $\mathcal{C} \subseteq \mathbb{Z}/n$ and let $\ell \colon \mathbb{Z}/n \to \mathbb{N}$. Then $\mathcal{C}$ is a *set of cuts with lengths* $\ell$ if $\mathcal{C}$ is not empty and for each $c \in \mathcal{C}$:

1. $1 \le \ell_c \le n$, $c - \ell_c \in \mathcal{C}$, and $c - d \notin \mathcal{C}$ for $1 \le d < \ell_c$;
2. $j \le \ell_c$, and the letters $c + k$ for $1 \le k \le j$ are thin.

The *arc* of $c$ is the set of letters $c - s$ with $0 \le s < \ell_c$. With $g = \max(G_0, S, \eta, 1)$, the *sizes are bounded by* $h$ if each letter is thin or has a size $b$ with $g < b$ and $b + S \le h$. There are *at most two thick letters per arc* if each arc has at most two letters that are not thin. For $a_0 \in \mathbb{N}$ the *word condition* $\mathrm{Word}(a_0)$ holds if for every cut $c$ and $s_0 < s_1 < \ell_c$:

1. if $c - s_1$ is down of size $b_1$ and $c - s_0$ is up of size $b_0$, then $b_0 < p b_1$;
2. if $c - s_1$ is up of size $b_1$ and $c - s_0$ is down of size $b_0$, then $2 b_0 \le p b_1$ and $2 a_0 < b_1$.

**Definition 8.5.3 (The exponent of Theorem E).** Fix $p, n, j, h$, the number $g$, cuts $\mathcal{C}$ with lengths $\ell$, and $H_1, H_2 \colon \mathbb{Z}/n \to \mathbb{N}$. Put $\ell^* = \max_{c \in \mathcal{C}} \ell_c$, $M = \lfloor (h + 2g)/(p - 1) \rfloor + 1$ and
$$\sigma = \Bigl\lceil \Bigl( 3g + \frac{M}{p^{j-1}} \Bigr) \frac{p}{(p-1)^2} + 1 \Bigr\rceil.$$
For $H \colon \mathbb{Z}/n \to \mathbb{N}$ let $H^* = \max_i H(i)$, $c_H = \lceil 1 + \log_p(H^* + 1) \rceil$ and
$$\begin{aligned} s_H(i) &= \sum_{a \ge 0} \frac{H(i + a + 1) + c_H + 3}{(p-1)^a}, \\ r_H(i) &= \Bigl\lfloor \min\bigl(\lfloor s_H(i) \rfloor, H^*\bigr) \frac{p}{(p-1)^2} \Bigr\rfloor + c_H, \end{aligned}$$
and $r = \max_{c \in \mathcal{C}} \max(r_{H_1}(c), r_{H_2}(c))$. Let $\mathcal{W}$ be the set of intervals $[a, a + t)$ of integers with $-2h \le a \le 2h$, $0 \le t \le 3g$ and $a + t \le 2h + 1$. For a finite set $J \subseteq \mathbb{Z}$ put $\nu(J) = \ell^* + \sum_{i \in J, i \ne 0} (\ell^* + 1 + v_p(i))$, and let $\kappa$ be the maximum of $\nu(w_1 \cup w_2 \cup w_3)$ over $w_1, w_2, w_3 \in \mathcal{W}$. Then
$$\begin{aligned} e_0 &= 2\sigma + r + 2 g \ell^*, \\ e &= 2r + 4\sigma + 2 e_0 + 2\kappa. \end{aligned}$$
We call $e_0$ the *initial exponent* and $e$ the *exponent of Theorem E*.

**Definition 8.5.4 (Theorem E for an ordering).** *Theorem E holds for* $\mathrm{emb}$ if the following is true. Assume the letter conditions and $p \ge 5$. Let $F \colon T_1 \to T_2$ be a map of crystalline lattices that is onto, with $T_1$ of good coefficients. Let $j, G_0, S, \eta, h \in \mathbb{N}$, kinds $\mathrm{ty}$, cuts $\mathcal{C}$ with lengths $\ell$, and $M_1, h_1, M_2, h_2 \colon \mathbb{Z}/n \to \mathbb{N}$ be such that:

1. the jumps of $T_1$ at each letter $i$ lie in the window of $\mathrm{ty}(i)$ for $G_0, S, \eta$, and all jumps of $T_1$ lie in $[-h, h]$;
2. $g \le h$, the sizes are bounded by $h$, $\mathcal{C}$ is a set of cuts with lengths $\ell$, and there are at most two thick letters per arc;
3. the jumps of $T_k$ are bounded by $(M_k, h_k)$ for $k = 1, 2$;
4. the word condition $\mathrm{Word}(e_0)$ holds, for the initial exponent $e_0$ with $H_k = M_k + h_k$.

Then $F$ lifts with exponent $e$, the exponent of Theorem E for $H_k = M_k + h_k$.

The hypotheses of the second form are a list of properties of $W$. Some are properties of Wach lattices that we name as in the earlier sections: P5, P6 (the exactness of saturation), P9 (described in the proof of [the lemma on level steps](/entry/lev-steps-of-jumps-prime/)) and the first property of Herr complexes. Two others we state. *Hodge exactness* says three things: for a map onto of crystalline lattices, each jump of $T_2$ is a jump of $T_1$; for a short exact sequence $0 \to T_0 \to T_1 \to T_2 \to 0$ with $T_1$ crystalline, $T_0$ and $T_2$ are crystalline and the jumps of $T_1$ at $\tau$ are those of $T_0$ and of $T_2$; and a lattice with trivial action has only the jump $0$. The *tools* say that $\varphi(\pi_0) = w \pi_0 q^{p-1}$ for a unit $w$, that each $\varphi^s(q)$ is a unit times $P(\pi_0)$ for a monic $P$ of degree $p^s$ whose lower coefficients are divisible by $p$, that $\varphi^s(q) - p \in (\pi_0)$, and that $\varphi^s(q) - p \in (q)$ for $s \ge 1$.

**Definition 8.5.5 (Hypotheses of the second form).** Let $C \in \mathbb{R}$. The *hypotheses of the second form* for $W$ and $C$ are: $s = 1$; $K_0 \to K$ is a bijection; $p \ge 5$; P5, P6 and P9; the Herr property; the properties $W_X$ and $W_R$ with constant $C$; the tools; the Frobenius properties F1 and F2; Hodge exactness; $\mathcal{O}$ is the valuation ring of $v$ and is $p$-adically complete; and there is a generator $e$ of $D(\mathbf{1})$ with the Bloch-Kato extension property such that the realisation of the arc data holds for $e$ and every ring condition on $W$.

**Proposition 8.5.6 (The Wach datum realises Theorem E).** Under the hypotheses of the second form, let $F$, $j, G_0, S, \eta, h$, $\mathrm{ty}$, $\mathcal{C}$, $\ell$ and $M_k, h_k$ satisfy conditions 1 to 4 of Theorem E. Then there are a base identification, coordinates $V_1, V_2, V_0$ of $T_1$, $T_2$ and $\mathbf{1}$ with a map $V_1 \to V_2$ over $F$, an element $e_0 \in V_0$, an irreducible $\varpi \in \mathcal{O}$, a number $e_{\mathcal{O}}$ and units $u, x \in \mathcal{O}^\times$ with $u = 1 + p x$, such that all the lattice hypotheses of the final form of Theorem E hold: the base condition for $(\varpi, e_{\mathcal{O}})$, the final lattice conditions for $V_1$ and $V_2$, the unit condition for $(V_0, e_0)$, the $\rho$-condition for the cocycles of $V_1$, the extension condition for the cocycles of $V_2$, the $W'$-condition at the cuts, and final arc data at every cut.

Lean: `Formalism.MainNotions.WachCoordinates.Br.realised_of`.

*Proof.* Since $p \ge 5$, $p \ne 2$. With $s = 1$ and $K_0 = K$, P9 gives the ring condition on $W$. The realisation of the arc data then gives the coordinates, the map, $e_0$ with $\theta_i(e_0) = e_i e$, and final arc data for every irreducible $\varpi$ at every cut. The ring condition, $s = 1$, the valuation ring and completeness give $\varpi$, $e_{\mathcal{O}}$ and $x$ with the base condition and $u = \chi_\Gamma(\gamma) = 1 + p x$. Since $p$ is not a unit in $\mathcal{O}$ and $|\Delta| = p - 1$ by P9, $|\Delta|$ is a unit. By the first part of Hodge exactness, the jumps of $T_2$ at each letter lie in the window of its kind, as those of $T_1$ do. P5, P6, P9 and the tools give the final lattice conditions for $V_1$ and $V_2$. The generator $e$ gives the unit condition. F1 and F2 give the $\rho$-condition. The Bloch-Kato extension property, Hodge exactness, $W_R$, $W_X$ and the bounds $(M_k, h_k)$ give the extension condition, and $W_R$, $W_X$ and the bounds $(M_k, h_k)$ give the $W'$-condition. $\square$

**Theorem 8.5.7 (Theorem E, second form).** Let $C \in \mathbb{R}$. If the hypotheses of the second form hold for $W$ and $C$, then Theorem E holds for the ordering $\mathrm{emb}$ of $W$.

Lean: `Formalism.MainNotions.WachCoordinates.Br.crystalline_lifting_second_form`.

*Proof.* Fix $F$ and the parameters, and take the data of the [last proposition](/entry/realised-of/). The numbers $\sigma$, $r$ and $\kappa$, with $g$, $h$ and $\ell^*$, satisfy the numerical conditions of the final form; this uses $p \ge 5$, the conditions on cuts, $g \le h$, the size bound, the bound on thick letters and the word condition $\mathrm{Word}(e_0)$. By the first part of Hodge exactness, the jumps of $T_2$ lie in $[-h, h]$. Let $Z(V_2)$ be the set of coordinate pairs of the Wach $\Delta$-cocycles of $T_2$ whose class is finite, and let $Z_F(V_1)$ be the analogous set for $T_1$ relative to $F$. F1 and F2, with the jumps of $T_1$ and $T_2$ in $[-h, h]$, give the $\rho$-condition for $Z_F(V_1)$. Now [the final form of Theorem E](/entry/theorem-e-final-form/) gives: for each $\kappa \in Z(V_2)$ there is $\kappa_1 \in Z_F(V_1)$ such that $p^{e} \kappa - h(\kappa_1)$ is a coboundary, with its exponent equal to the exponent $e$ of Theorem E. With $s = 1$, $p \ne 2$ and the Herr property for $T_2$, this says that $F$ lifts with exponent $e$. $\square$

**Remark 8.5.8 (Formalization).** Theorem E for an ordering is `ThmELiftAt` ([WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L123)), the hypotheses of the second form are `BrHyp2` ([CrystallineLiftingEveryOrdering.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineLiftingEveryOrdering.lean#L65)), and the realisation is `Realised` (ThmELiftAtOf.lean line 72). In `crystalline_lifting_second_form` the letter conditions are introduced as `_` and not used (line 160): the ordering is the one of $W$. In `realised_of` the word condition is introduced as `_` and not used (line 100); it is used only in the numerical step of the theorem. The constant $C$ enters only through `coreWR W C`. Not unfolded here: `coreWX`, `coreWR`, `F1`, `F2` (we read their shape but do not state them), `BKExt`, `UnitGen`, `PrimBase`, `FinalLat`, `PrimUnit`, `IsRho`, `PrimExt`, `WPrimeCuts` and the Herr property `p2aK`. `crystalline_lifting_every_ordering` (same file) passes to any ordering by a rotation of $\mathbb{Z}/n$.
