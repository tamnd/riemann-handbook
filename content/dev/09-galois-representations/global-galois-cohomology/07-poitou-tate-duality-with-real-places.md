---
title: Poitou-Tate duality with real places
decls:
  - GroundTheory.ProfCoh.bijective_tateCompactDualityMap_coind_gs_of_even
  - GroundTheory.ProfCoh.exists_tateCompactDualityHypotheses_gs_of_even
  - GroundTheory.ProfCoh.bijective_tateCompactDualityMap_gs_of_even
  - GroundTheory.ProfCoh.gsEvenTatePoitouTateHypotheses
  - GroundTheory.ProfCoh.gsTatePoitouTateHypotheses
  - GroundTheory.ProfCoh.injective_gsRealRes_three
  - GroundTheory.ProfCoh.bijective_gsRealRes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Poitou-Tate duality with real places

This section proves Poitou-Tate duality for $G_S$ when $K$ may have real places and the level $N$ may be even. Section 5 proved duality when $N$ is odd or $K$ is totally complex. Here the compact cohomology includes the real places, as in the previous section. For even $N$ we pass to open subgroups that fix $\mu_{2N}$. Their fixed fields contain $\sqrt{-1}$, so they are totally complex, and the case of Section 5 applies there. We then collect the hypotheses of the abstract Poitou-Tate theorem for every $N$. A consequence is that restriction to the real places is bijective on $H^r(G_S, M)$ for $r \geq 3$. The entry [The Euler ratio is one, from its coprime case](/entry/ratio-one-of-lemma-x/) in Volume 3 uses this with $r = 3$. The step [EveryCharacter from Row0b](/step/every-character-of-row/) depends on the duality.

### Setting

We keep the notation of the previous section. $K$ is a [[number field|MWBDFS2KJ5]] in $\overline{\mathbb{Q}}$, $S$ is a finite set of finite places, $G_S = \operatorname{Gal}(K_S/K)$, and $S_\mathbb{R}$ is the set of real places, with fixed embeddings at $S$ and at $S_\mathbb{R}$. Let $N \geq 1$, and assume that $S$ contains the places above $N$. Write $\mu_N \subseteq K_S$ for the $N$-th roots of unity. Since $S$ contains the places above $N$, $\mu_N \cong \mathbb{Z}/N$ as groups. For a finite module $M$ killed by $N$, let $M' = \operatorname{Hom}(M, \mu_N)$ be its dual. The groups $H^r_c$ are the compact groups with real places of the previous section. The theory is in [Galois cohomology of global fields](/learn/galois-cohomology/#global-fields) and [Selmer and Tate-Shafarevich groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups).

For $v \in S$, local class field theory gives the invariant $\operatorname{inv}_v : H^2(G_v, \mu_N) \to \mathbb{Q}/\mathbb{Z}$. For a real place $v$, the map $\mu_N \to \mathbb{C}^\times$ gives $\operatorname{inv}_v : H^2(G_v, \mu_N) \to H^2(G_v, \mathbb{C}^\times) = \tfrac12\mathbb{Z}/\mathbb{Z}$.

**Definition 2.7.1 (trace with real places).** The *trace* $t : H^3_c(G_S, \mu_N) \to \mathbb{Z}/N$ is a homomorphism with
$$t(\delta \xi) = \sum_{v \in S} \operatorname{inv}_v(\xi_v) + \sum_{v \in S_\mathbb{R}} \operatorname{inv}_v(\xi_v)$$
for each local family $\xi = (\xi_v) \in \bigoplus_{v \in S \cup S_\mathbb{R}} H^2(G_v, \mu_N)$, where $\delta$ is the map into $H^3_c$ and $\mathbb{Z}/N \subseteq \mathbb{Q}/\mathbb{Z}$.

Lean: `GroundTheory.ProfCoh.gsTrace` (also `GroundTheory.ProfCoh.gsTraceQZ`).

The trace exists. The kernel of $\delta$ is the image of $H^2(G_S, \mu_N)$, and the sum of the local invariants of a global class is $0$ by the reciprocity law for the Brauer group. So the sum of invariants factors through the image of $\delta$. Since $\mathbb{Q}/\mathbb{Z}$ is divisible, it extends to $H^3_c$. The values lie in $\frac1N\mathbb{Z}/\mathbb{Z}$, since $H^3_c$ is killed by $N$.

**Definition 2.7.2 (duality map).** For $r + s = 3$ the *duality map* is
$$H^r(G_S, M) \to \operatorname{Hom}\big(H^s_c(G_S, M'), \mathbb{Z}/N\big), \qquad x \mapsto \big(y \mapsto t(y \cup x)\big).$$

Lean: `GroundTheory.ProfCoh.tateCompactDualityMap`.

### The hypotheses of the abstract theorem

**Definition 2.7.3 (Poitou-Tate hypotheses with real places).** Let $D$ be a discrete $G_S$-module, $t : H^3_c(G_S, D) \to \mathbb{Z}/N$, and $\operatorname{inv}_v : H^2(G_v, D) \to \mathbb{Q}/\mathbb{Z}$ for $v \in S \cup S_\mathbb{R}$. The *Poitou-Tate hypotheses* for these data say, for each finite $M$ killed by $N$ with dual $M' = \operatorname{Hom}(M, D)$:

1. $D \cong \mathbb{Z}/N$ as groups;
2. the duality map is bijective for $r + s = 3$ and $s \geq 1$;
3. $H^r(G_S, M)$ is finite for $r \leq 2$;
4. $t \circ \delta$ is the sum of the local invariants on $\bigoplus H^2(G_v, D)$;
5. restriction $H^0(G_S, M) \to \prod_{v \in S} H^0(G_v, M)$ is injective, for every discrete $M$;
6. at each $v \in S$, the local cup product pairings of $H^0$ with $H^2$ and of $H^2$ with $H^0$ induce surjections onto the character groups;
7. at each real $v$, the pairing of $H^0(G_v, M)$ with $H^2(G_v, M')$ induces a surjection onto the characters, and every character of $H^0(G_v, M')$ that kills the norms comes from $H^2(G_v, M)$.

Lean: `GroundTheory.ProfCoh.TatePoitouTateHypotheses`.

Conditions 6 and 7 are local Tate duality at the finite places and Tate duality for $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$. From the hypotheses, an abstract argument gives the nine-term exact sequence, finiteness of the Tate-Shafarevich groups $\text{Ш}^1(M)$ and $\text{Ш}^2(M')$ with a perfect pairing between them, and the following fact.

**Lemma 2.7.4 (injectivity in degree $3$).** Under the hypotheses, restriction $H^3(G_S, M) \to \bigoplus_{v \in S \cup S_\mathbb{R}} H^3(G_v, M)$ is injective.

Lean: `GroundTheory.ProfCoh.TatePoitouTateHypotheses.injective_ptTGlobalToLocal_three` (also `GroundTheory.ProfCoh.TatePoitouTateHypotheses.nineTerm`, `GroundTheory.ProfCoh.TatePoitouTateHypotheses.sha`).

*Proof.* By the long exact sequence it is enough to show that $\delta : \bigoplus H^2(G_v, M) \to H^3_c(G_S, M)$ is surjective. By condition 2 with $(r, s) = (0, 3)$, applied to $M'$, the group $H^3_c(G_S, M)$ is dual to $H^0(G_S, M')$. Under this duality, $\delta$ is dual to the restriction of $H^0(G_S, M')$ to the places, by conditions 4, 6 and 7. That restriction is injective by condition 5. A homomorphism into $\mathbb{Q}/\mathbb{Z}$ extends along an injection, so $\delta$ is surjective. $\square$

### Even level

For even $N$, the difficulty is at the real places: $H^j(G_v, M)$ need not vanish. We remove it on small open subgroups.

**Theorem 2.7.5 (duality for coinduced modules, even level).** Let $N$ be even, and let $t : H^3_c(G_S, \mu_N) \to \mathbb{Z}/N$ be surjective. Let $W_0$ be an open subgroup of $G_S$ that fixes $\mu_{2N}$, and let $U \leq W_0$ be open. Then for $r + s = 3$ with $s \geq 1$, the duality map for $\operatorname{Coind}_U^{G_S} \mathbb{Z}/N$ is bijective.

Lean: `GroundTheory.ProfCoh.bijective_tateCompactDualityMap_coind_gs_of_even`.

*Proof.* Let $L$ be the fixed field of $U$. Since $4$ divides $2N$, $L$ contains $\sqrt{-1}$, so $L$ is totally complex. Let $v$ be a real place and $c \in G_v$ the complex conjugation. No conjugate $g c g^{-1}$ lies in $U$: it would fix $L$, but it is the complex conjugation for a real embedding and moves $\sqrt{-1}$. So each group $G_v \cap g^{-1} U g$ is trivial. By the Mackey formula, $H^j(G_v, \operatorname{Coind}_U^{G_S} \mathbb{Z}/N) = 0$ for $j \geq 1$, and the real places drop out. By Shapiro's lemma, the duality map becomes the duality map for $U = G_{L, S_L}$ with trivial coefficients $\mathbb{Z}/N$, compact cohomology without real places, and the trace $\tau = t \circ \operatorname{cor}$. Corestriction $H^3_c(U, \mu_N) \to H^3_c(G_S, \mu_N)$ is surjective, because $H^4_c$ vanishes on finite modules killed by $N$ by the previous section. So $\tau$ is surjective. The field $L$ is totally complex and $S_L$ contains the places above $N$. So by Section 5, the duality map at $U$ is bijective for every surjective trace. $\square$

**Definition 2.7.6 (Tate compact duality hypotheses).** For $D$, $t$ and an open subgroup $U_0$ of $G_S$, the *Tate compact duality hypotheses* say: $D \cong \mathbb{Z}/N$; $H^4_c(G_S, M) = 0$ for finite $M$ killed by $N$; and the duality map for $\operatorname{Coind}_U^{G_S} \mathbb{Z}/N$ is bijective for each open $U \leq U_0$ and each $r + s = 3$ with $s \geq 1$.

Lean: `GroundTheory.ProfCoh.TateCompactDualityHypotheses`.

**Theorem 2.7.7 (Tate compact duality hypotheses, even level).** Let $N$ be even and let $t : H^3_c(G_S, \mu_N) \to \mathbb{Z}/N$ be surjective. Then there is an open subgroup $U_0$ of $G_S$ such that the Tate compact duality hypotheses hold for $(N, \mu_N, t, U_0)$.

Lean: `GroundTheory.ProfCoh.exists_tateCompactDualityHypotheses_gs_of_even`.

*Proof.* The roots of unity $\mu_{2N}$ generate a finite extension of $K$ inside $K_S$, because $S$ contains the places above $2N$. Let $U_0$ be the open subgroup that fixes it. The first condition holds since $S$ contains the places above $N$. The second is the vanishing theorem of the previous section with $r = 4$. The third is the previous theorem with $W_0 = U_0$. $\square$

**Theorem 2.7.8 (duality, even level).** Let $N$ be even and let $t : H^3_c(G_S, \mu_N) \to \mathbb{Z}/N$ be surjective. Let $M$ be a finite discrete $G_S$-module with $NM = 0$. Then the duality map $H^r(G_S, M) \to \operatorname{Hom}(H^s_c(G_S, M'), \mathbb{Z}/N)$ is bijective for $r + s = 3$ and $s \geq 1$.

Lean: `GroundTheory.ProfCoh.bijective_tateCompactDualityMap_gs_of_even`.

*Proof.* Take $U_0$ from the previous theorem. The dévissage for the compact duality hypotheses then gives bijectivity for every finite $M$ killed by $N$. It treats $r = 0$ first, and then $r = 1$ and $r = 2$ in turn. Each step embeds $M$ into a sum of modules coinduced from small open subgroups and compares the two long exact sequences by the five lemma. The vanishing of $H^4_c$ closes the range at the top. $\square$

**Theorem 2.7.9 (Poitou-Tate hypotheses, even level).** Let $N$ be even. Then the Poitou-Tate hypotheses hold for $\mu_N$, the trace $t$ and the local invariants.

Lean: `GroundTheory.ProfCoh.gsEvenTatePoitouTateHypotheses`.

*Proof.* Since $N$ is even, $S$ contains the places above $2$, so $S$ is nonempty. The trace is surjective: by condition 4 it takes the value $1/N$ on the image of a local class of invariant $1/N$ at one $v \in S$. Condition 2 is the previous theorem. Condition 3 is the finiteness of $H^r(G_S, M)$ for $r \leq 2$. Condition 4 is the definition of $t$. Condition 5 holds because $S$ is nonempty and $G_v \to G_S$ is injective on $H^0$. Condition 6 is local Tate duality, and condition 7 is Tate duality for $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$ with coefficients in $\mu_N \subseteq \mathbb{C}^\times$. $\square$

### All levels

**Theorem 2.7.10 (Poitou-Tate hypotheses with real places).** Let $N \geq 1$ and assume that $S$ is nonempty and contains the places above $N$. Then the Poitou-Tate hypotheses hold for $\mu_N$, the trace $t$ and the local invariants.

Lean: `GroundTheory.ProfCoh.gsTatePoitouTateHypotheses`.

*Proof.* If $N$ is even, apply the previous theorem. Let $N$ be odd. For a real place $v$, the groups $H^j(G_v, M)$ with $j \geq 1$ are killed by $2$ and by $N$, so they are zero. So the compact cohomology with real places agrees with the compact cohomology of Section 5 in degrees $j \geq 1$. Section 5 gives duality for odd $N$, with a trace $t_{\mathrm{odd}}$. The other conditions are proved as in the even case. So the hypotheses hold for $t_{\mathrm{odd}}$. It remains to see that $t_{\mathrm{odd}} = t$. Both satisfy condition 4, so they agree on the image of $\delta$. By the lemma on degree $3$ and its proof, applied to $t_{\mathrm{odd}}$, $\delta$ is surjective onto $H^3_c(G_S, \mu_N)$. So $t = t_{\mathrm{odd}}$. $\square$

**Corollary 2.7.11 (Poitou-Tate duality with real places).** Under the conditions of the theorem, let $M$ be finite with $NM = 0$. Then the duality map is bijective for $r + s = 3$ and $s \geq 1$. The nine-term exact sequence of Poitou-Tate holds for $M$, with modified $H^0$ at the real places. The groups $\text{Ш}^1(G_S, M)$ and $\text{Ш}^2(G_S, M')$ are finite, and the cup product pairs them perfectly.

Lean: `GroundTheory.ProfCoh.poitouTateReal_duality` (also `GroundTheory.ProfCoh.poitouTateReal_compactDual`, `GroundTheory.ProfCoh.poitouTateReal_nineTerm`, `GroundTheory.ProfCoh.poitouTateReal_sha`).

### Restriction to the real places

**Theorem 2.7.12 (injectivity in degree $3$).** Assume that $S$ is nonempty and contains the places above $N$. Let $M$ be a finite discrete $G_S$-module with $NM = 0$. Then restriction
$$H^3(G_S, M) \to \prod_{v \in S_\mathbb{R}} H^3(G_v, M)$$
is injective.

Lean: `GroundTheory.ProfCoh.injective_gsRealRes_three`.

*Proof.* Let $x$ restrict to zero at each real place. At $v \in S$, the group $H^3(G_v, M)$ is zero, since $G_v$ has cohomological dimension $2$. So $x$ restricts to zero at every place of $S \cup S_\mathbb{R}$. By the theorem and the lemma on degree $3$, $x = 0$. $\square$

**Theorem 2.7.13 (restriction to the real places).** Assume that $S$ is nonempty and contains the places above $N$. Let $M$ be a finite discrete $G_S$-module with $NM = 0$, and let $r \geq 3$. Then restriction
$$H^r(G_S, M) \xrightarrow{\ \sim\ } \prod_{v \in S_\mathbb{R}} H^r(G_v, M)$$
is bijective.

Lean: `GroundTheory.ProfCoh.bijective_gsRealRes`.

*Proof.* The local groups at $v \in S$ are zero in degrees $3$ and higher. So in the long exact sequence of compact cohomology, the map from the real groups in degree $r$ goes to $H^{r+1}_c(G_S, M)$, which is zero by the previous section since $r + 1 \geq 4$. This gives surjectivity. For $r \geq 4$, injectivity follows in the same way from $H^r_c(G_S, M) = 0$. For $r = 3$ it is the previous theorem. $\square$

**Example 2.7.14.** Let $K = \mathbb{Q}$, $S = \{2\}$ and $M = \mathbb{Z}/2$. There is one real place, with group $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$ of order $2$. Its cohomology with coefficients $\mathbb{Z}/2$ is $\mathbb{Z}/2$ in each degree. So $H^r(G_{\mathbb{Q}, \{2\}}, \mathbb{Z}/2) \cong \mathbb{Z}/2$ for every $r \geq 3$, and the nonzero class restricts to the nonzero class of complex conjugation. If $K$ is totally complex, then $H^r(G_S, M) = 0$ for $r \geq 3$.

**Remark 2.7.15 (Formalization).** The trace is defined by choice, as some extension of the sum of the invariants ([RealTraceMap.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealTraceMap.lean#L42)). The odd case is proved with a second trace built from Section 5, and the proof shows that the two traces are equal ([NonemptyOfNatCastMemOfNeOne.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L40)). The statements take nonemptiness of $S$ as an instance argument, although the same file derives it from $N \neq 1$. The two restriction theorems include the embeddings at the places of $S$ as a variable, but their statements do not mention them ([NonemptyOfNatCastMemOfNeOne.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/NonemptyOfNatCastMemOfNeOne.lean#L131)). The odd case also has its own copies of the restriction theorems ([RealOddMain.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealOddMain.lean#L83)). The even case passes to totally complex fixed fields in [RealEvenTau.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealEvenTau.lean#L30) and uses the freeness of the real conjugates from [RealEvenFree.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/RealEvenFree.lean#L176).
