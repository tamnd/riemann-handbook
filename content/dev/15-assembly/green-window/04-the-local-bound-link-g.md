---
title: The local bound LinkG
decls:
  - Formalism.L2.G.loc_proved
  - Formalism.L2.G.local_model_results
  - Formalism.L2.G.admissible_family_no_kernel
  - Formalism.L2.G.linkG_without_kernels
  - Formalism.L2.G.linkG_fam_noKer
  - Formalism.L2.G.link_of_local_closed
  - Formalism.L2.G.linkG_concrete_noKer
  - Formalism.L2.G.linkG_concrete5
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local bound LinkG

This section proves that the local bound $\mathrm{Link}_G$ is closed on a family class, from group compatibility and one valuation condition. The proof goes through the nine admissibility conditions of a family, the first and second theorems at the family, and a record of local facts. The result is the input $\mathrm{Link}_G$ of [the shape theorem](/entry/shape-closed-link-n-of-green/), and through it of [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/). It is also used by [the remaining division bounds](/entry/b-rest-all-alt/).

We use the families of [the predicate Closed](/step/closed-def/). A family $F$ at scale $\varepsilon$ has a threshold $x_1$, index sets $I_x$, data $D(x,i)$, size data $L(x,i)$, an instance $G_x(x,i)$, a lattice instance $G_y(x,i)$ and constants $K$. Write $\mathrm{Ev}_F(P)$ for: there is $x_0$ such that $P(x,i)$ holds for all $x \ge x_0$ and all $i \in I_x$. $\mathrm{Closed}(\mathcal{C}, P)$ is the predicate Closed for the class $\mathcal{C}$.

**Definition 3.4.1 (The bound $\mathrm{Link}_G$).** $\mathrm{Link}_G(F)$ says: there are $C$, $x_0$ and a function $\delta$ with $\delta(x) \to 0$ such that for all $x \ge x_0$ and all $i$, the local bound $\mathrm{Link}_G^{\mathrm{at}}$ holds for $G_x(x,i)$ and $K$ with constant $C$ and error $b^{\delta(x)}$, where $b$ is a size parameter of $L(x,i)$. The local bound is a list: for each word $u$ and each place $w$ whose residue characteristic is not the prime of $u$, a lattice inclusion at depth $\lfloor \mathrm{ur}(D, w, \tau_w) \rfloor$ and a bound on lattice lengths; a bound $S_v \le 2 m N_v a / p$ for each prime $p$; at inert places below a cutoff, a bound of sums of the [[von Mangoldt function|0NK8JTE1NN]] over classes by the gains; and two orbit conditions.

**Definition 3.4.2 (The local record).** For a datum $D$, the *reduced second theorem* at $D$ says: for all constants $C_\Lambda, C_k, C_{rk}, C_{\deg}$, if $D$ is admitted for them (a list of 37 conditions) and two further existence conditions on constants hold, then the conclusion $\mathrm{E}(D)$ holds. Here $\mathrm{E}(D)$ says that there is $C_0 > 0$ such that $\mathrm{aux}_3(D, C)$ holds for each $C \ge C_0$. The statement $\mathrm{aux}_3(D, C)$ is a long statement on a prime $p \ge 13$, discrete valuation rings in an unramified quadratic setting and numerical inequalities, with conclusion $\mathrm{LP}'$. The *local record* $\mathrm{Loc}$ is the statement that the reduced second theorem holds at every datum $D$.

**Theorem 3.4.3 (The local record).** $\mathrm{Loc}$ holds.

Lean: `Formalism.L2.G.loc_proved`

*Proof.* Let $D$ be a datum. [Statement E](/entry/stmt-e/) gives: for all constants, if $D$ is admitted, then $\mathrm{E}(D)$. The reduced second theorem follows: drop the two further conditions and apply Statement E to the constants and to the proof of admission. $\square$

**Theorem 3.4.4 (Local model results).** $\mathrm{Loc}$ implies the record $\mathrm{Loc}_6$ of seventeen local facts: the reduced second theorem at every $D$; the [second part in closed form](/entry/second-part-closed/) at every $D$; three counts; seven statements on Fock models and lattices and a Witt identity; and four conditions on each $D$. The counts are these, with $s(\lambda)$ the number of index sets for a dominant $\lambda \in \mathbb{Z}^n$:

1. the number of index sets for a sequence $\mu_0, \dots, \mu_N$ with dominant last term $\lambda$ is $\prod_{i<j} \frac{\lambda_i - \lambda_j + j - i}{j - i}$;
2. $s(\nu) = \sum_\mu s(\mu)$ for $\nu \in \mathbb{Z}^{m+1}$, over the $\mu \in \mathbb{Z}^m$ with $\nu_{i+1} \le \mu_i \le \nu_i$;
3. $s(\nu) \binom{b+m}{m} = \sum_\mu s(\mu)$, over the $\mu$ such that $\mu/\nu$ is a horizontal strip of size $b$, and the same with the strip below $\nu$.

Lean: `Formalism.L2.G.local_model_results`

*Proof.* The first field is the hypothesis. Each other field is a proved lemma. The counts are the Weyl dimension formula for $\mathrm{GL}_n$, a branching rule by interlacing and a Pieri rule, proved through Gelfand-Tsetlin patterns. $\square$

**Definition 3.4.5 (Admissible families).** The nine *admissibility conditions* $\mathrm{Adm}_1(F), \dots, \mathrm{Adm}_9(F)$ are conditions of the form $\mathrm{Ev}_F$ on the data, the instances and the constants. $\mathrm{Adm}_2$ is a valuation condition. The family *admissibility* $\mathrm{Adm}(F, K, G_x, G_y)$ joins them for a choice of instances. The condition $\mathrm{NPDesc}(F)$ is a descent condition on Newton polygons. For a lattice instance $Y$, let $Y^0$ be $Y$ with each chain replaced by the zero chain.

**Theorem 3.4.6 (Admissibility without kernels).** Let $F$ be a family with $\mathrm{Adm}_1(F), \dots, \mathrm{Adm}_9(F)$. Assume that, eventually, each local datum of $D(x,i)$ has trivial stabilisers and finitely many classes, the operators of $D(x,i)$ preserve the lattices, the orbit lattice bounds hold for $(G_x, G_y)$, and the lattice sandwich holds for $G_x$. Assume $\mathrm{NPDesc}(F)$. Then $\mathrm{Adm}(F, K, G_x, G_y^0)$ holds, and eventually the unit bound at twisted places and the first gluing condition hold for $(G_x, G_y^0)$.

Lean: `Formalism.L2.G.admissible_family_no_kernel`

*Proof.* The valuation clauses ask that the image of a vector under a chain lies in a scaled lattice $\varpi^{\lceil g v \rceil} N$. For the zero chain the image is $0$, which lies in each lattice, so these clauses hold for each $g$. The rest of the gluing condition comes from the gluing statement, with the stabiliser, operator, orbit and sandwich facts. [The stability of trivial stabilisers](/entry/stability-of-trivial-stabilisers/) and the service statement give the other parts. $\square$

**Theorem 3.4.7 ($\mathrm{Link}_G$ without kernels).** Under the hypotheses of the last theorem, $\mathrm{Link}_G(F)$ holds.

Lean: `Formalism.L2.G.linkG_without_kernels`

*Proof.* The [admissibility without kernels](/entry/admissible-family-no-kernel/) gives $\mathrm{Adm}(F, K, G_x, G_y^0)$ and the gluing condition. [Statement F](/entry/stmt-f/), a proved family theorem, turns admissibility into $C$ and $\delta$ with $\delta(x) \to 0$ and the family conclusion with error $b^{\delta(x)}$. A lemma turns this conclusion, the gluing condition and four facts on $G_x$ into $\mathrm{Link}_G^{\mathrm{at}}$ with constant $4|C| + 1$. The facts are the served indices, the bound on $S_v$, the served values and the lattice lengths; the last one uses $\mathrm{NPDesc}(F)$. The bound $\mathrm{Link}_G$ reads only $G_x$ and $K$, so the change of $G_y$ does not matter. $\square$

**Theorem 3.4.8 ($\mathrm{Link}_G$ for one family).** Let $F$ be a family. Assume the second theorem at $F$, the first theorem at $F$, $0 < K.\mathrm{La}$, $1 \le C_e$, and eventually $N_1 \le K.C_N \log x$. Assume that eventually each local datum has trivial stabilisers and finitely many classes and has a standard subring. Assume $\mathrm{Adm}_2(F)$, $\mathrm{NPDesc}(F)$ and the window log bound for $F$. Then $\mathrm{Link}_G(F)$.

Lean: `Formalism.L2.G.linkG_fam_noKer`

*Proof.* The proof builds the hypotheses of [$\mathrm{Link}_G$ without kernels](/entry/link-g-without-kernels/). $\mathrm{Adm}_6$ comes from the second theorem, $\mathrm{Adm}_7$ from a kappa bound, $\mathrm{Adm}_8$ from the first theorem, and $\mathrm{Adm}_9$ from a Weyl sandwich with the constant $C_e$. $\mathrm{Adm}_1$, $\mathrm{Adm}_3$, $\mathrm{Adm}_4$ and $\mathrm{Adm}_5$ come from four family lemmas; $\mathrm{Adm}_3$ uses an order estimate with constant $100$ from the CM field lemmas. The orbit lattice bounds come from a linear programming input, the sandwich from $\mathrm{Adm}_9$, and the operators preserve the lattices for every datum. $\square$

**Theorem 3.4.9 ($\mathrm{Link}_G$ from local data).** Let $\mathcal{C}$ be a family class. Assume $\mathrm{Loc}$ and that these four predicates are closed on $\mathcal{C}$: eventually trivial stabilisers and finitely many classes; eventually standard subrings at each place (a discrete valuation ring in an unramified quadratic setting with a finite map to the given ring); $\mathrm{Adm}_2$; and $\mathrm{NPDesc}$. Then $\mathrm{Closed}(\mathcal{C}, \mathrm{Link}_G)$.

Lean: `Formalism.L2.G.link_of_local_closed`

*Proof.* The [local model results](/entry/local-model-results/) and [the second theorem with an absolute constant](/entry/second-theorem-absolute-constant/) give one $C_0 \ge 0$ with $\mathrm{aux}_3(D, C_0)$ for all $D$, and so the second theorem at each family. The local model results and the local flatness results give the first theorem at each family. The constant conditions and the window log bound are closed on every class. Join the ten closed statements and apply [$\mathrm{Link}_G$ for one family](/entry/link-g-fam-no-ker/). $\square$

**Definition 3.4.10 (Group compatibility).** $\mathrm{GC}(F)$ says: eventually, for each $i$, the datum $D(x,i)$ has a compatibility record. The record has a Hermitian datum and forms for each word, a compatibility of the lattice comparison, a ring compatibility at each place, and a field that writes each local datum as the datum of a level at the residue prime.

**Theorem 3.4.11 ($\mathrm{Link}_G$ from group compatibility).** Let $\mathcal{C}$ be a family class. Assume $\mathrm{Loc}$, $\mathrm{Closed}(\mathcal{C}, \mathrm{GC})$ and $\mathrm{Closed}(\mathcal{C}, \mathrm{Adm}_2)$. Then $\mathrm{Closed}(\mathcal{C}, \mathrm{Link}_G)$.

Lean: `Formalism.L2.G.linkG_concrete_noKer`

*Proof.* Apply [$\mathrm{Link}_G$ from local data](/entry/link-of-local-closed/). Group compatibility gives the three other closed hypotheses: the trivial stabilisers from the Hermitian levels and the level field, the standard subrings from the ring compatibility, and $\mathrm{NPDesc}$ from the comparison. $\square$

**Theorem 3.4.12 (The concrete $\mathrm{Link}_G$).** Let $\mathcal{C}$ be a family class with $\mathrm{Closed}(\mathcal{C}, \mathrm{GC})$ and $\mathrm{Closed}(\mathcal{C}, \mathrm{Adm}_2)$. Then $\mathrm{Closed}(\mathcal{C}, \mathrm{Link}_G)$.

Lean: `Formalism.L2.G.linkG_concrete5`

*Proof.* This is [$\mathrm{Link}_G$ from group compatibility](/entry/link-g-concrete-no-ker/) applied to [the local record](/entry/loc-proved/). $\square$

**Remark 3.4.13 (Formalization).** All theorems except the last two are in [AdmissibleFamilyNoKernel.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L188): `admissible_family_no_kernel` at line 188, `linkG_without_kernels` at 224, `linkG_fam_noKer` at 241, `link_of_local_closed` at 272, `loc_proved` at 284 and `local_model_results` at 43. The last two are in LinkGConcreteNoKer.lean, lines 48 and 54.

- The term $\mathrm{aux}_3(D, C)$ takes $D$ as `_D` and never reads it. So $\mathrm{E}(D)$ is the same statement for every $D$, and the second theorem enters only as one constant.
- The two further conditions of the reduced second theorem are never used; `criterion_restricted_of_closed` ignores them.
- `local_model_results` uses its hypothesis for one field only. The field names `rationalPlanesClauseThree`, `Four` and `Five` hide a Weyl dimension formula, a branching count and a Pieri count, and these counts take an unused argument `_D`.
- `extremal_projector_tools_of_loc` (line 40) and `local_flatness_results` (line 62) take $\mathrm{Loc}$ and do not use it.
- `admissible_family_no_kernel` takes $\mathrm{NPDesc}(F)$ and does not use it. The zero chain (`zeroCh`, line 166) makes the valuation bounds vacuous (`vKge_zero`, line 178). This is sound, since $\mathrm{Link}_G$ reads only $G_x$. The orbit lattice bounds are asked for $G_y$, not $G_y^0$.
- `linkG_fam_noKer` uses one of the eight conclusions of `field_lemmas_except_seven`, which is in the namespace `UnusedSlot33` (CMFieldLemmas.lean line 21).
- The suffix 5 of `linkG_concrete5` is not explained. The same file has `linkG_concrete` (line 35), which needs two more hypotheses on local data systems.
- We have not unfolded $\mathrm{Adm}_2$, $\mathrm{NPDesc}$, $\mathrm{LP}'$, the conclusion of the first theorem, or the terms of $\mathrm{Link}_G^{\mathrm{at}}$.
