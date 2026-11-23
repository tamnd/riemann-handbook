---
title: Wach data and the local Theorem C
decls:
  - Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_literature_hypotheses
  - Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_local_lemmas
  - Formalism.MainNotions.RamifiedCoefficientChains.S9.bigCellDetWeightedEnergyIntegral.dual_lemma_of_admitted
  - Formalism.MainNotions.RamifiedCoefficientChains.Asm.lemmaGs_rec
  - Formalism.MainNotions.RamifiedCoefficientChains.S9.LocalLemmasFromLiterature.local_lemmas_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Wach data and the local Theorem C

The local Theorem C is a second bound on the colength of a map of lattices that is onto. In Theorem B each letter has its own kind; here the window of jumps alternates with the parity of the letter, and the bound has a third term that counts the jumps of $T_2$ near $0$. We introduce Wach data, prove two lemmas on Wach modules and a bridge from cocycles to Wach vectors, and prove Theorem C with the constant $25$. The theorem is used in [Theorem C of admitted inputs](/entry/theorem-c-of-admitted-inputs/).

We keep the notation of [the local Theorem B](/entry/thm-b-at/): a period datum with prime $p$, the fields $K_0 \subseteq K$ with $n = [K_0 : \mathbb{Q}_p]$, the letters $i \in \mathbb{Z}/n$ with embeddings $\mathrm{emb}_i$, the coefficient field $L$ with ring $\mathcal{O}$, and the valuation $v$ of $L$ with $v(p) = 1$.

**Definition 8.2.1 (Ring of letters).** The *ring of letters* is $\Lambda = \prod_{i \in \mathbb{Z}/n} \mathcal{O}[[X]]$. Let $e_i \in \Lambda$ be the idempotent of the letter $i$. Given an endomorphism $\varphi_0$ of $\mathcal{O}[[X]]$, the Frobenius of $\Lambda$ is $\varphi(a)_i = \varphi_0(a_{i-1})$: it moves the letter $i - 1$ to the letter $i$.

Since $L$ contains the images of all embeddings of $K_0$, the ring $\mathcal{O} \otimes_{\mathbb{Z}_p} \mathcal{O}_{K_0}[[X]]$ of Wach modules with coefficients splits as a product over the embeddings, and the Frobenius $\sigma$ of $K_0$ permutes the factors. This is why $\varphi$ shifts the letters.

**Definition 8.2.2 (Wach datum).** A *Wach datum* for a period datum and a coefficient field consists of:

1. a level $s \ge 1$, with $s \ge 2$ if $p = 2$;
2. an endomorphism $\varphi_0$ of $\mathcal{O}[[X]]$ with $\varphi_0(X) = X q_0$, where $X q_0 = (1+X)^p - 1$;
3. a quotient $\Gamma$ of $G$ with an injective character $\chi_\Gamma \colon \Gamma \to \mathcal{O}^\times$ compatible with the cyclotomic character, an action $\delta \mapsto \delta_0$ of $\Gamma$ on $\mathcal{O}[[X]]$, an element $\gamma$ with $v(\chi_\Gamma(\gamma) - 1) = s$, and the finite set $\Delta$ of torsion elements of $\Gamma$;
4. a $p$-adically complete ring $E \supseteq \Lambda$ in which $X$ is invertible, with actions of $\varphi$ and $\Gamma$;
5. for each lattice $T$, a free $E$-module $D(T)$ of the rank of $T$ with commuting semilinear actions of $\varphi$ and $\Gamma$, and a finitely generated $\Lambda$-submodule $N(T) \subseteq D(T)$, the *Wach module*;
6. functorial maps $D(T) \to D(T')$ for maps of lattices $T \to T'$;
7. a comparison map $N(T) \to V \otimes_{\mathbb{Q}_p} B$ with values in $D_{\mathrm{cris}}(V)$ that kills $X N(T)$ and sends $e_i N(T)$ to the part of $D_{\mathrm{cris}}(V)$ at $\mathrm{emb}_i$;
8. maps from Herr cocycles on $D(T)$ to the cohomology of $T$, and level maps $\Lambda \to L[[X]]$ for each letter $i$ and each $\zeta \in L$.

For crystalline $T$ the Wach module spans $D(T)$ over $E$, it is stable under $\Gamma$, $(\gamma - 1) N(T) \subseteq X N(T)$, and the poles of $\varphi$ on $N(T)$ are bounded by powers of elements of the type of $q_0$. These are the properties of the Wach modules of Wach and Berger; see [Wach modules](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals). Put
$$\pi_0 = 1 - p + \sum_{\delta \in \Delta} \delta_0(1 + X), \qquad q = \pi_0 + p,$$
both read in every letter. If $|\Delta| = p - 1$, then $\pi_0 = \sum_{\delta \in \Delta} (\delta_0(1+X) - 1)$, a trace of $X$ over $\Delta$. Let $\Lambda^\Delta$ be the $\Delta$-invariants of $\Lambda$. For a letter $i$ let $N_i(T)$ be the set of $x \in N(T)$ with $e_i x = x$ and $\delta x = x$ for all $\delta \in \Delta$, and let $D_i(T)$ be the image of $N_i(T)$ in $D_{\mathrm{cris}}(V)$.

**Definition 8.2.3 (Setting of Theorem C).** Let $d \in \mathbb{N}$, let $F \colon T_1 \to T_2$ be a map of lattices, $b \colon \mathbb{Z}/n \to \mathbb{N}$ and $S, \eta, m \in \mathbb{N}$. Write $h = \max_i b_i + S$ and $H = h + \eta$, and put
$$\lambda(l, H) = \log_l(2H) + 1, \qquad a_R(l, H) = \frac{H(2l - 1)}{(l-1)^2} + 3 + \lambda(l, H).$$
Read $i$ in $\{0, \dots, n-1\}$. The *window* of the letter $i$ is $[-b_i - S, -b_i] \cup [-\eta, \eta]$ if $i + d$ is even and $[b_i, b_i + S] \cup [-\eta, \eta]$ if $i + d$ is odd. We are in the *setting of Theorem C* if:

1. we are in case A ($K_0 = K$, $s = 1$, $p \ne 2$), $p \ge 11$, and $n$ is even;
2. $\mathcal{O}$ is a discrete valuation ring with fraction field $L$, and $L$ contains a primitive $p$-th root of unity;
3. $T_1$ and $T_2$ are crystalline and $F$ is onto;
4. for each letter $i$ and each $\tau$ over $i$, the jumps of $T_1$ at $\tau$ lie in the window of $i$;
5. for each $\tau$, the multiplicities of the jumps of $T_2$ at $\tau$ in $[-\eta, \eta]$ add up to at most $m$;
6. $2 a_R(p, H) + \eta + 1 \le b_i$ and $h/2 \le b_i$ for every letter $i$.

In this setting the jumps of $T_1$ are bounded by $(M, h')$ with $M_i = b_i + S$, $h'_i = \eta$ when $i + d$ is even and $M_i = \eta$, $h'_i = b_i + S$ when $i + d$ is odd. Let $e'_C$ be the [lifting exponent](/entry/thm-b-at/) of $T_1$ for these bounds.

The *admitted inputs* of Theorem C are nineteen statements from the theory of Wach modules and the comparison theorems. Two more inputs are taken as given: the *bound on core jumps* and the *condition on letters*.

**Lemma 8.2.4 (Frobenius lemma at odd letters).** Assume the admitted inputs, the bound on core jumps and the condition on letters. Let $\ell$ be a prime and $(K, L)$ good at level $1$, and take the Wach datum at $(\ell, K, L)$. Let $F$, $d$, $b$, $S$, $\eta$, $m$ be in the setting of Theorem C and let $i$ be a letter with $i + d$ odd. Then there is $E \in \mathbb{N}$ with
$$E \le \frac{3 a_R(p, H) + S + 2\eta}{p - 1} + \lambda(p, H)$$
such that every $x \in \varphi^2(D_{i-2}(T_2))$ with $x \in D_{\mathrm{cris}}(V_2) \cap \mathrm{Fil}^{b_i}$ satisfies $p^{k} x \in \mathrm{cmp}(F(N_i(T_1)))$, where
$$k = \Bigl\lceil E + \frac{2H}{(p-1)^2} + 1 + b_{i-1} + S - b_i \Bigr\rceil.$$

Lean: `Formalism.MainNotions.RamifiedCoefficientChains.Asm.lemmaGs_rec`.

*Proof.* The lemma is assembled from two parts. The first part is proved from the admitted inputs alone. The second uses also the bound on core jumps and the condition on letters. The two parts combine to give the exponent $E$. $\square$

**Lemma 8.2.5 (Dual lemma at even letters).** Assume the admitted inputs. Let $\ell$, $(K, L)$ and the Wach datum be as above, let $F$, $d$, $b$, $S$, $\eta$, $m$ be in the setting of Theorem C, and let $i$ be a letter with $i + d$ even. Let $r = \dim_L V_2$, let
$$c_D = \frac{H + 1}{p - 1} + 1,$$
and let $P_i \subseteq D(T_2)$ be the $\mathcal{O}$-span of the elements $a \varphi(x)$ with $a \in \Lambda^\Delta$ and $x \in N_{i-1}(T_2)$. Then there is a set $s \subseteq N_i(T_2)$ with at most $m$ elements such that
$$\operatorname{length}_{\mathcal{O}} \frac{N_i(T_2)}{\pi_0 N_i(T_2) + q^{b_i + S} P_i + \operatorname{span}_{\mathcal{O}} s} \le \bigl( rS + 2 m c_D \bigr) \lambda_{\mathcal{O}},$$
where $\lambda_{\mathcal{O}} = \operatorname{length}(\mathcal{O}/p\mathcal{O})$.

Lean: `Formalism.MainNotions.RamifiedCoefficientChains.S9.bigCellDetWeightedEnergyIntegral.dual_lemma_of_admitted`.

*Proof.* We are in case A, so the level is $s = 1$, and $p \ge 11$ gives $p \ge 5$. In case A the admitted inputs give the ring condition on the Wach modules, and the tie between the Wach datum and the cyclotomic character gives the action of $\gamma$. The admitted level tools give the behaviour of the level maps on the Hodge filtration. From these we get rules for the exponents of $q$, the points of the level maps and their coefficients, a basis tool, and a membership criterion. Next, $|\Delta| = p - 1$ is a unit in $\mathcal{O}$. Indeed $p$ lies in the maximal ideal and $p - (p-1) = 1$; if $p - 1$ were in the maximal ideal too, so would be $1$. So we may divide by $|\Delta|$, that is, average over $\Delta$. With this unit we build a truncation tool, a basis adapted to $\varphi$, and a determinant tool from the points of the level maps and condition 5 of the setting. The length bound then follows from the determinant statement at the even letters. $\square$

**Theorem 8.2.6 (From cocycles to Wach vectors).** Assume the admitted inputs, the bound on core jumps, the properties of Herr classes for the natural extension, the comparison of Fontaine on filtrations, and the Fontaine core statement in case A. Let $\ell$, $(K, L)$ and the Wach datum be as above and let $F$, $d$, $b$, $S$, $\eta$, $m$ be in the setting of Theorem C. Then there is $s_0 \in \mathbb{N}$ with
$$s_0 \le \frac{2\lceil a_R(p, H) \rceil + 2\eta + S}{p - 1} + \lambda(p, H) + 2\sigma + 2,$$
where $\sigma$ depends only on $p$, $h$ and $\eta$, with the following property. For every finite free $\mathcal{O}$-module $\Phi$ with a map $g \colon \Phi \to Z^1_f(T_2)$, there are a submodule $\Phi_2 \subseteq \Phi$ and, for each even letter $c$, a map $w_c$ from $\Phi_2$ to $D(T_2)$, such that:

1. $\Phi_2$ is joined to $\Phi$ by a chain of at most $n$ steps, each with a quotient generated by $m$ elements, and $\Phi_2 = \Phi$ if $m = 0$;
2. each $q^\eta w_c(f)$ lies in the pull-back of $N_{c-1}(T_2)$ by $\varphi$, and $w_c(f)$ is a *Wach vector* at $c$: it lies in the part of letter $c$, it is fixed by $\Delta$, it has finite poles, and $\gamma w_c(f) - w_c(f) \in \pi_0 N(T_2)$;
3. for each $f \in \Phi_2$ there are cocycles $\kappa_c$ attached to $w_c(f)$ by the Herr class maps with $p^{s_0} g(f) \mp \sum_c \kappa_c \in B^1(T_2)$.

Lean: `Formalism.MainNotions.RamifiedCoefficientChains.S9.LocalLemmasFromLiterature.local_lemmas_of_literature`.

*Proof.* The set-up is the one of the dual lemma: case A with $s = 1$ and $p \ge 5$, the ring condition, the action of $\gamma$, the level maps on the filtration, the exponent rules, the basis tool, and the unit $|\Delta|$. Two lifting steps follow. The first starts from $\pi_0$ and the admitted results on Wach modules. The second uses the truncation tools and the admitted Frobenius congruences. Then an extension tool is built from the properties of Herr classes, the comparison of Fontaine on filtrations, the bound on core jumps, the Fontaine core statement, and an inverse of $|\Delta|$ in $\mathcal{O}$. These give the bound. $\square$

**Theorem 8.2.7 (Local Theorem C).** Fix the period data and the Wach data at every prime. Assume the bound on core jumps and the condition on letters, and assume that the admitted inputs imply the theorem from cocycles to Wach vectors at every good $(\ell, K, L)$. If the admitted inputs hold, then the following is true. Let $\ell$ be a prime, $(K, L)$ good at level $1$, and $F$, $d$, $b$, $S$, $\eta$, $m$ in the setting of Theorem C, with $p = \ell$; let $r$ and $c_D$ be as in the dual lemma. Then there is $e \in \mathbb{N}$ with
$$e \le \frac{32 H}{\ell^2} + 4S + \frac{10 \eta}{\ell - 1} + 25 \lambda(\ell, H)$$
such that $\operatorname{col}(F) \le x \cdot \lambda_{\mathcal{O}}$, where
$$\begin{aligned} x = {} & (n+1) r e + 4 n m e'_C \\ & + \tfrac{3}{2} n \bigl( r S + 2 m c_D \bigr), \end{aligned}$$
and such that, if $m = 0$, $F$ lifts with exponent $e + 3S$.

Lean: `Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_local_lemmas`.

*Proof.* Assume the admitted inputs. Three local bounds give the theorem. The first is the theorem from cocycles to Wach vectors, which holds by assumption. The second is a chain bound at each even letter $c$. It gives an exponent $e$ such that Wach vectors $w$ at $c$ as in condition 2 above lift after multiplication by a power of $p$, with $e$ added to the exponent, to elements $F(u)$ modulo $\pi_0 N(T_2)$, with $u$ a Wach vector of $T_1$. The lift holds on a submodule reached by a chain of $6$ steps generated by $m$ elements and $3$ steps of length at most $(rS + 2 m c_D) \lambda_{\mathcal{O}}$; if $m = 0$ it holds everywhere, with exponent $e + 3S$. The chain bound comes from a Wach vector lifting bound and a bound at the sixth step. The lifting bound is proved from the Frobenius lemma at odd letters, the dual lemma at even letters, a second dual lemma at the letter $0$, and a bound on $H^2$, all from the admitted inputs. The third bound, from the admitted inputs, says that a Wach vector that lifts in this way gives a cocycle $\kappa_c$ in the image of $H^1(T_1)$ after the same power of $p$.

Together the three bounds give the local lifting conditions. The exponent $e + s_0$ moves each finite class of $T_2$ into the image, along a chain of submodules whose steps are counted by the two chain bounds; and if $m = 0$ the map $F$ lifts with exponent $e + s_0 + 3S$. The assembly then uses the lifting theorem in case A and the theorem on generators of finite classes, both among the admitted inputs, as in the [counting step](/entry/thm-b-at/) of Theorem B. It gives the bound with the constants $32$, $4$, $10$, $4$, $\tfrac{3}{2}$ and $25$. $\square$

**Corollary 8.2.8 (Theorem C from the literature).** Assume the bound on core jumps, the condition on letters, the properties of Herr classes for the natural extension, the comparison of Fontaine on filtrations, and the Fontaine core statement in case A. If the admitted inputs of Theorem C hold, then the conclusion of the local Theorem C holds with the constant $25$.

Lean: `Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_literature_hypotheses`.

*Proof.* This is the local Theorem C, with its assumption on the bridge supplied by the theorem from cocycles to Wach vectors. $\square$

**Remark 8.2.9 (Formalization).** The admitted inputs are `RamifiedCoefficientChains.admitted`, the conjunction `adm1` to `adm19`, and the statement proved is `Stmt` with $C = 25$, that is `admitted → aux₃ 25`, with `aux₃ = ConclusionL`. `ConclusionL` quantifies over a predicate $R$ on $m$ that is always `True` ([RamifiedCoefficientChains.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L139)), so $R$ has no effect. `SetCS` (line 60) requires $n$ even and $p \ge 11$, so the theorem says nothing for odd $n$. `LetterConditionGlobal` takes an argument `_F` that it does not use, and it enters only through `lemmaGs_rec`. Not unfolded here: `lemGA_rec`, `lemGB_rec`, `lemmaDN_of_S1E`, `cocyclesToWachVectorsBound_of_extTool`, `steps6_of`, `rhoLift_of_Adm`, `stmt_of_lemmas`, `sig` and `RhoCoc`. The dual lemma lives in a namespace `bigCellDetWeightedEnergyIntegral` whose name has no relation to its content. The two proofs repeat the same set-up nearly line for line (UniformizerClauseOfAdmitted.lean lines 57 to 93, UniformizerClauseOfAdmittedAlt.lean lines 56 to 91), and both run with `maxHeartbeats 0`. The inputs `adm22` and `adm23` exist twice with the same bodies, in `CrystallineLiftingBounds` (lines 106 and 109) and in `LiftingTheory` (lines 647 and 650).
