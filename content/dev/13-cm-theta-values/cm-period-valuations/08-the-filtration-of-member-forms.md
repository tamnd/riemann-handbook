---
title: The filtration of member forms
decls:
  - GlobalTheory.StabTopLaw.xiTop_stab_law
  - GlobalTheory.T.lastStepDatum_law_topLevelStabilizer
  - GlobalTheory.KerJ.term_law
  - GlobalTheory.T.classSum_term_law_stabiliser_target
  - GlobalTheory.KFiClose.kFi_of_tie
  - GlobalTheory.T.kernelClassSums_carry_chainComplexForms
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The filtration of member forms

The kernel condition of Section 6 has four global parts. One of them, the *filtration condition*, says that the kernel operator of each chain sends the forms of level $i$ to the forms of level $i + 1$. This section proves it. The forms at a level are cut out by laws under a stabilizer group, so the proof reduces to one identity for each stabilizer element: the *term law*. We prove the term law level by level. The hardest case is the top level, where the identity is a product formula over places. The filtration condition is used in [the kernel condition over true columns](/entry/at-of-true-columns/).

### Forms cut out by stabilizers

Let $u$ be a word and let $C$ be a column chain for $u$, with classes $C_i$ at each level $i$, points $Y_i$ at level $i$, and a kernel operator $K_i$ that sends functions on the classes at level $i$ to functions on the classes at level $i + 1$. A family of member forms $M$ over $C$ gives a set $\mathrm{Fi}_i(M)$ of functions $\varphi \colon C_i \times Y_i \to \mathbb{C}$ at each level $i$. For the datum $D$ we have the member chain of $u$ with the forms $\mathrm{Fi}_i(u)$, and for each tuple $\mu$ the twisted chain $C_{u, \mu}$. A twist $\tau$ gives the forms of $\tau$ at $(u, \mu)$ on $C_{u, \mu}$.

**Definition 5.8.1 (Filtration condition).** Let $\tau$ be a twist of $D$. The pair $(D, \tau)$ satisfies the *filtration condition* if:
1. for every word $u$, every $i < m$ and every $\varphi \in \mathrm{Fi}_i(u)$, we have $K_i \varphi \in \mathrm{Fi}_{i+1}(u)$;
2. for every word $u$, every used tuple $\mu$, every $i < m$ and every form $\varphi$ of $\tau$ at $(u, \mu)$ of level $i$, the image of $\varphi$ under the kernel operator of $C_{u, \mu}$ is a form of $\tau$ of level $i + 1$.

An *object* $O$ over $C$ has a frame map $\mathrm{frm}_i$ at each level: for each point $y \in Y_i$ and each embedding $\tau$ of $E$ it gives a complex matrix $\mathrm{frm}_i(y)_\tau$. It also has kernel series $\Theta_{i, c, c'}$ for $c \in C_i$ and $c' \in C_{i+1}$. These are functions on families $z = (z_\tau)$ of $N(i) \times N(i+1)$ matrices.

**Definition 5.8.2 (Stabilizer law).** Let $g$ be an $N(i) \times N(i)$ matrix over $E$ and $k \in \mathbb{C}$. A function $f$ on $Y_i$ satisfies the *law* of $(g, k)$ if $f(y) = k f(y')$ whenever $\mathrm{frm}_i(y)_\tau = \tau(g)\, \mathrm{frm}_i(y')_\tau$ for every $\tau$. Let $G$ be stabilizer data: a set $G_i(c)$ of pairs $(g, k)$ for each level $i$ and class $c$. The forms $M$ are *cut out by* $G$ if every form of level $i \le m$ has values of the right kind at every class, and if for $1 \le i \le m$ a function $\varphi$ is a form of level $i$ exactly when each $\varphi(c)$ has values of the right kind and satisfies the law of every pair in $G_i(c)$.

**Definition 5.8.3 (Term law).** Let $c \in C_i$, $c' \in C_{i+1}$, $g$ an $N(i+1) \times N(i+1)$ matrix over $E$ and $k \in \mathbb{C}$. The pair $(g, k)$ satisfies the *term law* at $(i, c, c')$ if $\det g \ne 0$ and there is $\kappa \in \mathbb{C}$ with

$$
\begin{aligned}
\Theta_{i, c, c'}\big(\tau(g)\, z_\tau\big) &= \kappa\, \Theta_{i, c, c'}(z) \quad \text{for all } z,\\
k &= \kappa \prod_\tau \tau(\det g)^{-s_i(\tau)}.
\end{aligned}
$$

Here $s_i(\tau)$ are the weights of the chain at level $i$.

The term law says that the series $\Theta_{i, c, c'}$ is an eigenvector of left translation by $g$, and that the eigenvalue matches $k$ after the weight factor. This is what one needs to move the law of $(g, k)$ through the kernel operator.

### The top level

The kernel entry $t$ carries a field triple $(E, F, K)$, a finite set of primes with a set $V_G$ of good places, characters at each level, a selection of places of $E$ over the places of $F$, a tuple, local constants and level indices. The local constants have a flag *sharp* and two integers $A$ and $M$. We write $m = m_2 + 2$. The top datum $\Xi_{\mathrm{top}}(p, Y, p', x)$ depends on a chain point $p$ at level $m_2 + 1$, a set $Y$ of vectors, a chain point $p'$ at level $m_2 + 2$ and a linear map $x$. The places of the row are the places in $V_G$ together with the places of the selection over the primes of the tuple. At a place $P$ of the row, $\mu_P$ is the local character at level $m_2 + 1$. The frame group at level $m_2 + 2$ consists of pairs $a = (\gamma, (a_G, a_Q))$, with $\gamma$ a linear automorphism and with $a_G$ and $a_Q$ local components at the good places and at the places of the tuple. The twist characters at the top are $\chi_{\mathrm{Lt}}$ on the good part and $\chi_{\mathrm{Tt}}$ on the tuple part.

**Theorem 5.8.4 (Top-level stabilizer law).** Assume that the fields, the primes and the selection are in order, that the primes $g_i$ and $T_v$ lie in the bad set, that the level indices and the characters are in order, that the local constants are sharp, that $m \le A$, that the numbers $h_j(b, P)$ of the level indices equal $1$ at the good places $P$ for $j \le m_2 + 1$, and that $2M$ is at most the top depth of the ranks. Let $p$ be a chain point at level $m_2 + 1$, $Y$ a set in the admissible family of $p$, $p'$ a chain point at level $m_2 + 2$, and $a$ an element of the frame group with $a \cdot p' = p'$. Then for every $x$

$$
\begin{aligned}
&\Xi_{\mathrm{top}}(p, Y, p', \gamma \circ x) \prod_P \mu_P(\det \gamma)\\
&\quad = \chi_{\mathrm{Lt}}(a_G)\, \chi_{\mathrm{Tt}}(a_Q)\, \Xi_{\mathrm{top}}(p, Y, p', x),
\end{aligned}
$$

where the product runs over the places $P$ of the row.

Lean: `GlobalTheory.StabTopLaw.xiTop_stab_law` (also `GlobalTheory.T.lastStepDatum_law_topLevelStabilizer`, a second name)

*Proof.* The top datum is a product: a global factor $\phi_T(p, p', x)$ times local factors $\mathrm{top}_P$, one for each place $P$ of the row, evaluated at the map $x$ read in the frames $F_P$ of $p$ and $F'_P$ of $p'$. The global factor does not change under $x \mapsto \gamma \circ x$, because $a$ fixes $p'$.

Since $a$ fixes $p'$, for each place $P$ there is a local element $\kappa'_P$ with $\gamma F'_P \kappa'_P = F'_P$. So the map $\gamma \circ x$, read in the frames, is $\kappa_P'^{-1}$ composed with $x$ read in the frames. Taking determinants gives $\det \gamma = \det(\kappa_P')^{-1}$. The element $\kappa'_P$ is integral with integral inverse, so its determinant reduces to a unit, and $\mu_P(\det \gamma) = \rho_P(\det \kappa'_P)$ for the local character $\rho_P$.

The twist character splits as a product over the places of the row: the good places carry the components of $a_G$ and the places of the tuple carry the components of $a_Q$. This uses that the good places and the places of the tuple are disjoint. So it is enough to prove one identity at each place $P$: the factor $\mu_P(\det \gamma)$ times the local factor at the moved map equals the local character of $a$ at $P$ times the local factor at $x$. At a good place this is the law of the local top datum, applied to the vectors of $Y$; it uses the properties of the admissible family and a fact on the coupling index at $P$. At a place of the tuple it uses a lemma on the scaled coupling index and a lemma on the twist character at the top depth. The second lemma needs the bound $2M \le$ top depth. The product of the local identities and the invariance of the global factor give the claim. $\square$

### The term law at every level

The pinned stabilizers of $t$ at $(u, \mu)$ are stabilizer data $G$ with chain points at each level, indices, admissible sets $Y$ at level $m_2 + 1$ and points at the top, such that the reads of $t$ are the entry data $\Xi_{\mathrm{entry}}$ at levels $i < m_2$, the coupling data $\Xi_{\mathrm{cpl}}$ at level $m_2$, and the top data at level $m_2 + 1$, and such that $G_i(c)$ is the stabilizer of the chain point at each level. At level $m_2 + 1$ the stabilizer must also preserve $Y$. The entry $t$ satisfies the *column side conditions* if its fields, primes, selection and characters are in order, its bad set contains the primes $g_i$, $T_v$, the small primes and $q$, its constants are sharp with $m \le A$ and $2M$ at most the top depth, and the numbers $h_j(b, P)$ of its level indices equal $1$ at the good places.

**Theorem 5.8.5 (Term law for pinned stabilizers).** Let $t$ be a tied kernel entry that satisfies the column side conditions. Let $u$ be a word, $\mu$ a tuple and $G$ pinned stabilizers of $t$ at $(u, \mu)$. Then for every $i < m$, all classes $c \in C_i$ and $c' \in C_{i+1}$, and every $(g, k) \in G_{i+1}(c')$, the pair $(g, k)$ satisfies the term law at $(i, c, c')$ for the object of $t$ at $(u, \mu)$.

Lean: `GlobalTheory.KerJ.term_law` (also `GlobalTheory.T.classSum_term_law_stabiliser_target`, a second name)

*Proof.* A lemma on pair kernels turns a law for a finite datum into the term law. It asks for a function $f$ that gives the reads of $t$ after the embedding $\sigma_0$, an element $\gamma$ that preserves the lattice at level $i + 1$, invariance of $f$ under translation by the level lattice, and the identity

$$
f(\gamma \circ x) \prod_P \mu_P(\det \gamma) = k f(x).
$$

We check these in three cases. Each pair in $G_{i+1}(c')$ comes from an element $a$ that fixes the chain point. If $i < m_2$, then $f$ is the entry datum. It is invariant under the level lattice, and the stabilizer law of the entry datum gives the identity. If $i = m_2$, then $f$ is the coupling datum, with the same two facts for it. If $i = m_2 + 1$, then $f$ is the top datum. Its invariance under the level lattice comes from the primes of the twist, and the identity is the top-level stabilizer law above. $\square$

### The filtration condition

**Theorem 5.8.6 (Filtration from pinned forms).** Let $t$ be a tied kernel entry for $\mathrm{ex}$. Assume that $t$ satisfies the column side conditions and that its forms are pinned: for every word $u$ and every used tuple $\mu$ there are stabilizer data $G$ that cut out the forms of the twist of $\mathrm{ex}$ at $(u, \mu)$ and that are pinned stabilizers of $t$. Then $(D, \tau)$ satisfies the filtration condition, where $\tau$ is the twist of $\mathrm{ex}$.

Lean: `GlobalTheory.KFiClose.kFi_of_tie` (also `GlobalTheory.T.kernelClassSums_carry_chainComplexForms`, a second name)

*Proof.* Take a word $u$ and a used tuple $\mu$, and let $G$ be the pinned stabilizers. A lemma on kernel operators says: if forms are cut out by $G$, the object is unfolded, the kernel tie is entire at every level, and every pair of $G$ satisfies the term law, then the kernel operator sends forms of level $i$ to forms of level $i + 1$. The object of $t$ is unfolded, its kernel tie is entire, and the term law holds by the previous theorem. This proves part 2 of the filtration condition. The base tuple $\mu_0$ is used. A lemma on the reference tuple carries part 2 at $\mu_0$ to the member forms of $D$, and this is part 1. $\square$

**Remark 5.8.7 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.lastStepDatum_law_topLevelStabilizer`, `GlobalTheory.T.classSum_term_law_stabiliser_target` and `GlobalTheory.T.kernelClassSums_carry_chainComplexForms` are second names, proved by `first | exact @… | …` under `maxHeartbeats 1000000`.
2. In `GlobalTheory.StabTopLaw.xiTop_stab_law` four hypotheses are introduced and never used: `hTS` (the primes $T_v$ lie in the bad set), `hCh` (the characters are in order), `hA` ($m \le A$) and `hb` ($h_j(b, P) = 1$ at the good places) (LastStepDatumLawTopLevelStabilizer.lean:23). The theorem holds without them. The top datum `XiTop`, the family `ybSet`, the local factor `topDat` and the characters `muAt` are not unfolded here.
3. The filtration condition `OrbitPlaces.KFi` (OrbitPlaces.lean:107) depends only on $D$ and the twist, not on the entry $t$. At the use site the entry is a second entry $t'$ from the column record. The second name speaks of "class sums" and "chain complex forms", which do not appear in the statement.
4. In `GlobalTheory.KerJ.term_law` one fact of `t.rd_chain` is discarded with `-` (ClassSumTermLawStabiliserTarget.lean:29). The three cases rely on $m = m_2 + 2$.
5. The definitions `FormsAre`, `TermLaw` (FormsAre.lean:22 and :28), `StabPin`, `FormsPin` and `ColSide` (FormsPin.lean:19, :37, :40) were opened. The predicate `IsVal` ("values of the right kind") is not unfolded.
