---
title: Rows from kernel chains
decls:
  - GlobalTheory.T.memberRows_of_kernelDatum_sizes
  - GlobalTheory.ColRows.rowsBody_of_kerTies
  - GlobalTheory.T.columnsMemberRows_of_logLevel_le
  - GlobalTheory.ColRowsTopS.rowsBody_colFace
  - GlobalTheory.T.kernelHalf_chainNumbers_any_levelPrime
  - GlobalTheory.KernelHalfS.kerSide_chainS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rows from kernel chains

This section proves the body of the row statement at one member of a definite side. It is used by [the rows from the column pins](/entry/rows-u-of-col-pins-alt/), which takes the constant $C_0$ from it, in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The row statement factors the column period of a member through a chain of explicit matrices, and it bounds the norm of each step. The bounds on the steps come from the kernel chain of the member, and they are proved by averaging bounds for theta vectors over the embeddings of a number field.

### The data

Let $K$ be a totally complex field of a field record, and let $v$ run over the infinite places of $K$. Let $m$ be the rank of the datum and put $n = m - 2$. A *definite side* gives, for each tuple $t$ with a base tuple $\mu_0$, a dimension $n_V(t)$ and a hermitian matrix $H_V(t)$ over $K$. The *column face* gives, for each member $x$, a dimension $a(x)$, a frame matrix $X_c(x)_v$ for each $v$, from the hermitian lattice of the member, and for each $t$ a pairing $P(x, t) : K^{a(x)} \to (K^{n_V(t)})^{\vee}$, the *column period*.

The *kernel chain* $Q$ of $x$ at $\mu_0$ has hermitian families $F_0, \ldots, F_n$ with step maps $F_j \to F_{j+1}$, a last hermitian space $S_1$ and a map $\mathrm{col} : F_0 \to S_1$. There is a linear map $f_0 : K^{a(x)} \to F_0$, the inclusion of the columns.

The *row body* at $x$ asks for the following.

1. A chain of dimensions $c_0 = a(x), \ldots, c_{n+1}$, invertible frames $X_i$ at each $v$ with $X_0 = X_c(x)$, matrices $K_j$ from $K^{c_j}$ to $K^{c_{j+1}}$, and a last map $P_L$, such that $P(x, \mu_0)(\varphi) = P_L(K_n \cdots K_0 \varphi)$.
2. A tie of this chain to $Q$: maps from $K^{c_i}$ to $F_i$ and to $S_1$ that are isometries for the frames $X_i$, that turn $K_j$ into the step map for $j < n$ and $K_n$ into the map to $S_1$, and whose first map is $f_0$.
3. Frames $Y_v$ with $(Y_v^{-1})^{\ast} Y_v^{-1} = H_V(\mu_0)$.
4. Height numbers $h$ for the record of numbers $R$, such that the squared operator norm of $P_L$ at $v$, from $X_{n+1}$ to the dual frame of $Y$, is at most $e^{h_P}$.
5. Column bound data whose log sizes at step $j$ are at most the sum of the size heights $h_{\mathrm{sz}}(l, v)$ over the indices $l$ that map to $j$.

The record $R$ holds the numbers $f$, $m$, $N$, $L$, $L_a$, $\log T$, the mean $\log \Omega$ of the logarithmic period, the weights $\nu_{j, \tau, i}$ and a constant $C_h$. It *reads* the datum if these are the numbers of the datum at the member.

### The bounds on the kernel chain

**Theorem 7.15.1 (Bounds on the kernel chain).** For each real $C_Y$ there is $C \geq 0$ with the following property. Take a member with level prime $T$ and its kernel chain $Q$. Assume the host, weight, character and analytic ties, that the tuple at $\mu_0$ is $1$ with a sharp constant, that the field is a field of definition, the size conditions with constant $C_Y$, and that $R$ reads the datum. Then there are numbers $g_0(j)$, $A(j, v)$, $\log \Omega(\tau, v)$, $\log \theta_0(v)$, $\log h(j)$, $\log h'(j)$, $\mathrm{vv}$ and $\log g$, for $j$ in an index set of size $m$, such that the following hold.

1. The mean of $\log \Omega(\tau, \cdot)$ over the places is the number $\log \Omega$ of $R$, and the mean of $\log \theta_0$ is at most $C L$.
2. The bounds

$$\begin{aligned} A(j, v) &\leq C f m^2 N^2 (\log g + \log T) + C f N^2 \log g, \\ \log h(j),\ \log h'(j) &\leq C f N^2 (L + \log T + \log g), \\ \log g &\leq C L \end{aligned}$$

hold.
3. $0 \leq g_0(j) \leq N^2$, and both $\log(8 + 32\, |P|\, g_0(j)\, \mathrm{vv})$ and $\log(2 \sum_i \nu_{j, \tau, i} + 2)$ are at most $C L_a$.
4. Let $t(j, v)$ be the lifted map size built from these numbers. For each step $i < n$, each $v$ and each $\varphi$,

$$\operatorname{Re} \langle \mathrm{step}\, \varphi, \mathrm{step}\, \varphi \rangle_v \leq e^{t_i(v)} \operatorname{Re} \langle \varphi, \varphi \rangle_v,$$

where $t_i(v)$ is the sum of $t(j, v)$ over the $j$ that map to step $i$. The same holds for the last map to $S_1$, with the sum over the remaining $j$.

Lean: `GlobalTheory.T.kernelHalf_chainNumbers_any_levelPrime` (also `GlobalTheory.KernelHalfS.kerSide_chainS`).

*Proof.* The constant is a sum of constants $C_K$, $C_c$, $C_i$, $C_y$, $C_t$ and $C_Y$ of the lemmas below, with $C = C_K + 2(C_c + C_i + C_y) + 2 \max(C_t, 0) + 20 + 2 \max(C_Y, 0)$.

1. The class numbers and the index counts at each level are at most $\exp((C_c + C_i + C_y) E)$, with $E = f m^2 N_m^2 \log(g_0 g_1 T)$.
2. There is a number field $M$ that contains the coefficients of the theta data. On the embeddings of $M$ over each infinite place of $K$ there are weights with sum $1$ and the right mean.
3. The log norms of the vacuum vector at each embedding $\rho$ of $M$ are given by a rank product formula. Their mean is at most $2 \max(C_t, 0) f L$, by [the norm bound for normalized families](/entry/normalised-family-norm-bound-absolute-constant/) of section 16.
4. The mean of $\log \Omega$ is the mean period of the generator.
5. The numbers of steps 1 to 4 satisfy claims 1 to 3. The size bounds of claim 3 use the size conditions with constant $C_Y$.
6. The step maps of $Q$ are bounded at each $\rho$ by the norms of the matrix steps of the coupled factor, with constant $C_K$, at any level prime. Average these bounds with the weights of step 2. This gives claim 4.

The rest is bookkeeping. $\square$

### The row body

**Theorem 7.15.2 (Row body at one member).** For all reals $C_Y$ and $C_T \geq 0$ there is $C_0$ with the following property. Take a member $x$ with word $u$ and level prime $T$, and assume the following:

1. the host, weight, character and analytic ties; the tuple at $\mu_0$ is $1$ with a sharp constant; the field is a field of definition;
2. the size conditions with constant $C_Y$, and $\log T \leq C_T\, m\, L$;
3. $R$ reads the datum and $C_0 \leq C_h$;
4. $H_V(\mu_0)$ is positive definite at each $v$;
5. for each frame $Y$ as in item 3 of the row body, $\operatorname{Re} \langle \mathrm{ev}\, F, \mathrm{ev}\, F \rangle_v \leq \|F\|_{Y, v}^2$ for the evaluation map.

Then the row body holds at $x$, and $\det X_c(x)_v$ is a unit at each $v$.

Lean: `GlobalTheory.T.columnsMemberRows_of_logLevel_le` (also `GlobalTheory.ColRowsTopS.rowsBody_colFace`).

*Proof.* Let $C \geq 0$ be the constant of [the bounds on the kernel chain](/entry/kernel-half-chain-numbers-any-level-prime/) for $C_Y$. Put

$$C_0 = \max\bigl(2(16 + C_T),\ 6C + 1 + 2C^2,\ 4C(C_T + C)\bigr).$$

1. The bounds on the kernel chain bound each step map of $Q$.
2. The level prime satisfies $T \geq 1$. With $\log T \leq C_T m L$, the last map has a bound with the number $\ell_{\mathrm{last}}$ of the last log size.
3. The two bounds give height numbers $h$ with $h_P = \ell_{\mathrm{last}}$. This needs the three lower bounds on $C_h$ that enter $C_0$.
4. Positive definiteness gives frames $Y$ as in item 3. The map $f_0$ is an isometry, and its frame matrices have unit determinant. This gives the second conclusion.
5. The factorization lemma for kernel chains gives the row body from frames of all the families, the factorization $P = g \circ \mathrm{col} \circ f_0$ with $g$ the pairing on $S_1$, and a bound

$$|g(\psi)(F)|_v^2 \leq e^{h_P} \operatorname{Re} \langle \psi, \psi \rangle_v\, \|F\|_{Y, v}^2.$$

The factorization holds by the definition of the column period.
6. The bound of step 5 is the norm bound for branching maps between interlacing weights, with members of the same shift, combined with hypothesis 5 and $\langle \psi, \psi \rangle_v \geq 0$.

This proves the theorem. $\square$

### Tied kernel entries

A record $t$ of kernel entries tied to a datum $D$ with size data $L$ holds a field record, primes, characters, a word $t(u)$ for each word $u$ of $D$, and a tuple, a constant and a character index for each tuple of $D$, with a level $m_2$. For $\Delta, h_0 \in \mathbb{N}$ let $N$ be the number datum of $D$, $L$, $\Delta$ and $h_0$. The record is *tied* if the host, weight and character ties hold for $N$, the analytic tie holds for $D$, the tuple at $\mu_0$ is $1$ with a sharp constant, $m_2 = m - 2$, and the field is a field of definition at every word. It has *sizes* $C_Y$ and $C_T$ if the size conditions hold with constant $C_Y$ at the letter of each word and $\log T(u) \leq C_T\, m\, L$ for each word $u$.

**Theorem 7.15.3 (Row body for tied kernel entries).** For all reals $C_Y$ and $C_T \geq 0$ there is $C_0$ with the following property. Let $t$ be a tied record of kernel entries with sizes $C_Y$ and $C_T$, with a totally complex field. Take column data at each tuple, pulled back from $D$ by a map of tuples that fixes $\mu_0$, a word $u$, and the record of numbers $R$ built from $N$, the letter of $u$, $T(u)$ and seven reals with their facts. Assume $C_0 \leq C_h$, that the matrix at the base tuple is positive definite at each infinite place, and the bound for the evaluation map. Then the row body holds at $u$, and the frames of the hermitian lattice at $t(u)$ have unit determinant.

Lean: `GlobalTheory.T.memberRows_of_kernelDatum_sizes` (also `GlobalTheory.ColRows.rowsBody_of_kerTies`).

*Proof.* Take $C_0$ from [the row body at one member](/entry/columns-member-rows-of-log-level-le/). Read each tie and size condition. The level prime of $t(u)$ is $T(u)$. The record $R$ built from $N$ reads the datum. Substitute $m_2 = m - 2$ and apply the theorem. $\square$

**Remark 7.15.4 (Formalization).** The statements `T.memberRows_of_kernelDatum_sizes` at line 8 of [MemberRowsOfKernelDatumSizesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizesStatement.lean#L8), `T.columnsMemberRows_of_logLevel_le` at line 11 of [ColumnsMemberRowsOfLogLevelLeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnsMemberRowsOfLogLevelLeStatement.lean#L11) and `T.kernelHalf_chainNumbers_any_levelPrime` at line 10 of [KernelHalfChainNumbersAnyLevelPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrimeStatement.lean#L10) are `first | exact` relays. The tied form is `rowsBody_of_kerTies` at line 10 of [MemberRowsOfKernelDatumSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizes.lean#L10); it uses every field of the two structures `KerTies` and `KerSizes`, but few fields of the record `KerEntTied`. The row body is `rowsBody_colFace` at line 25 of [ColumnsMemberRowsOfLogLevelLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnsMemberRowsOfLogLevelLe.lean#L25). The kernel bound is `kerSide_chainS` at line 219 of [KernelHalfChainNumbersAnyLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrime.lean#L219), with the packing `kerSide_of_meansS` at line 104. The size predicate `SizeRowsS` has a conjunct `True` at line 16 of [ColHeightSharpWith.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ColHeightSharpWith.lean#L16). A second theorem `ColRowsTop.rowsBody_colFace`, at line 109 of [IpAtNonnegOfDatFramed.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IpAtNonnegOfDatFramed.lean#L109), has the same short name, four more hypotheses, the older size predicate and the number $25$ in place of $C_T$; the index of uses shows no use of it.
